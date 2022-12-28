# Office Coincidence 

This repository contains a small programming exercise. 

**Exercise**

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

## Setting up your environment

For the coding exercise you will need Python and Pytest:

Once you installed Python you can install pytest with pip

```
pip install pytest
```

## How to use

To get started:

💻 Clone the repo `git clone https://github.com/carlosandresat/office_coincidence`

🏃 Run the main script by using terminal in the office_coincidence directory:

```
python script.py
```

or (depending on your environment variables)

```
py script.py
```

🧪 To run the tests you can use `pytest -v` since there are not more test files in directory


## The solution

I created a the `officeSchedule` class to encapsulate the necessary methods. The class takes as parameter a string with the filename of the data text file and in its initialization, it calls to `getData()` method to fill the data attribute of the created instance. (The data is stored in a list of lists `[[]]`)

The data structure is represented as

```
[['employee1', 'Day', startTime, endTime, 'Day', startTime, endTime, ...], ['employee2', 'Day', ...], ...]
[['RENE', 'MO', 10.0, 12.0, 'TU', 10.0, 12.0, 'TH', 1.0, 3.0, 'SA', 14.0, 18.0, ...], ['ASTRID', ...
```

To go through each day of an employee is used a `for loop` in the range of `(len(employee)-1)/3`. In this way I can access to:

- Employee name: employee[0]
- Days worked: employee[1+3*i]
- Start hours: employee[2+3*i]
- End hours: employee[3+3*i]

where `i` is the for loop iterator and employee, and `employee` is one of the list inside `data`.

The method `haveCoincidence()` calculates if there is a coincidence between two working times. To count the total number of coincidences from one employee with another, is used `countCoincidence()` that takes two employee data and go through the data in the way mentioned before. And finally the `officeCoincidence()` method that use two loops to compare each employee with the others without repeating pairs.

The code creates an instance of the class with `data.txt` as path, and run the `officeCoincidence()` method to print all the pairs of workers with their number of times they were together at work at the same time.
