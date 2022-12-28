from script import officeSchedule
import pytest

@pytest.fixture
def office():
    return officeSchedule('data.txt')

def test_when_data_file_is_wrong_formatted():
    with pytest.raises(ValueError):
        officeSchedule('wrong-data.txt')

@pytest.mark.parametrize(
    "start_a,start_b,end_a,end_b,expected",
    [
        (8, 14, 13.9, 16.5, False),
        (8, 12, 12, 16, True),
        (8, 10, 16, 14, True),
        (12, 8, 16, 12, True),
        (14, 8, 16.5, 13.9, False)
    ]
)

def test_haveCoincidence(office, start_a, start_b, end_a, end_b, expected):
    assert office.haveCoincidence(start_a, start_b, end_a, end_b) == expected

def test_if_countCoincidence_counts_more_than_data_lenght(office):
    for i in range(len(office.data)-1):
        assert office.countCoincidence(office.data[i], office.data[i+1]) <= min(len(office.data[i]), len(office.data[i+1]))