from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, fname, lname):
        self.Firstname = fname
        self.Lastname = lname

    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, fname, lname, salary):
        self.Firstname = fname
        self.Lastname = lname
        self.Salary = salary

    def get_salary(self):
        return self.Salary


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hoursWorked, rate):
        self.Firstname = fname
        self.Lastname = lname
        self.HoursWorked = hoursWorked
        self.Rate = rate

    def get_salary(self):
        return (self.HoursWorked * self.Rate)


fte1 = FullTimeEmployee("John", "Smith", 1500)
he1 = HourlyEmployee("Mary", "Jane", 30, 45)

print(f"{fte1.Firstname} {fte1.Lastname} earned {fte1.get_salary()}")
print(f"{he1.Firstname} {he1.Lastname} earned {he1.get_salary()}")
