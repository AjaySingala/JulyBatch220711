# class Person:
#     City = "Boston"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John Smith", 42)
# p2 = Person("Mary Jane", 35)

# print(f"Name: {p1.name}. Age: {p1.age}, City: {p1.City}")
# print(f"Name: {p2.name}. Age: {p2.age}, City: {p1.City}")

class Person:
    # constructor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printFullname(self):
        print(self.lastname + ", " + self.firstname)

    # def printFullname(self, message):
    #     print(f"{message} : {self.firstname}")

p1 = Person("John", "Smith")
print(p1.firstname, p1.lastname)
p1.printFullname()
# p1.printFullname("some message")

p2 = Person("Mary", "Jane")
p2.printFullname()
# p2.printFullname("Hello there, ")

class Student(Person):
    def __init__(self, lname, fname, year):
        #super().__init__(fname, lname)
        #Person.__init__(self, fname,lname)
        self.firstname = fname
        self.lastname = lname
        self.graduationYear = year

    def printFullname(self):
        #print("Hello there, " + self.firstname + " " + self.lastname + ". You are from the class of ", str(self.graduationYear))
        print(f"Hello there {self.firstname} {self.lastname}. You are from the class of {self.graduationYear}")

    def welcome(self):
        # print("Welcome " + self.firstname + " " + self.lastname + " to the class of ", str(self.graduationYear))
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationYear}")

s1 = Student("Doe", "John", 2019)
s1.printFullname()
s1.welcome()
#s1.printFullname("this is a custom message")

s2 = Student("stark", "tony", 1997)
s2.printFullname()
s2.welcome()

print("\nEmployee and Manager")
class Employee(Person):
    pass

class Manager(Employee):
    pass

e1 = Employee("John", "Smith")
m1 = Manager("Mary", "Jane")
e1.printFullname()
m1.printFullname()

print("\nCheck instance types...")
print(isinstance(p1, Person))
print(isinstance(s1, Student))
print(isinstance(p1, Student))
print(isinstance(s1, Person))

# class Car:
#     color = ""

#     def __init__(self, _color):
#         self.color = _color

#     def start(self):
#         print(f"My color is {self.color}")

# c1 = Car("Red")
# print(isinstance(c1, Person))
# print(c1.color)
# c1.start()
