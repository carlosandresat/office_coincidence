class officeSchedule:
    def __init__(self, path: str) -> None:
        self.path =  path
        self.data = self.getData()

    def getData(self):
        with open(self.path) as f:
            data = []
            for line in f:
                employee = []
                name = line.split('=', 1)[0]
                employee.append(name)
                week = line.split('=', 1)[1].split(',')
                for day in week:
                    dayName = day[:2]
                    employee.append(dayName)
                    start = int(day[2:4]) + int(day[5:7])/60
                    employee.append(start)
                    end = int(day[8:10]) + int(day[11:13])/60
                    employee.append(end)
                data.append(employee)
        return data
    #[['RENE', 'MO', 10.0, 12.0, 'TU', 10.0, 12.0, 'TH', 1.0, 3.0, 'SA', 14.0, 18.0, ...], ['ASTRID', ...

    def haveCoincidence(self, start1, start2, end1, end2) -> bool:
        return max(start1, start2) <= min(end1, end2)

    def countCoincidence(self, emp1, emp2) -> int:
        count = 0
        for i in range(int((len(emp1)-1)/3)):
            for j in range(int((len(emp2)-1)/3)):
                if(emp1[1+3*i] == emp2[1+3*j]):
                    if(self.haveCoincidence(emp1[2+3*i], emp2[2+3*j], emp1[3+3*i], emp2[3+3*j])):
                        count = count+1
        return count

    def officeCoincidence(self):
        for employee1 in range(len(self.data)-1):
            for employee2 in range (employee1+1, len(self.data)):
                count = self.countCoincidence(self.data[employee1], self.data[employee2])
                print(self.data[employee1][0] + "-" + self.data[employee2][0] + ": " + str(count)) if count else None

path = 'data.txt'
acme = officeSchedule(path)
acme.officeCoincidence()