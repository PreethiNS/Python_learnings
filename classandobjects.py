class NewClass:
    x= 50
print(NewClass.x)

class NewClass1:
    x= 100
#create object
r= NewClass1()
print(r.x)

class Student:
    id = 10
    name = 'anderson'
    def display(self):
        print(self.id,self.name)
student1 = Student()
student1.display()

class Student:
    """ This is a student class"""
    age = 14
    def welcome(self):
        print(f"Hi, welcome to section B")
print(Student.age)
print(Student.welcome)
print(Student.__doc__)

#init function
class Student:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
s1 = Student("pree","26/2/2000")
print(s1.name,s1.dob)
#modify objects
s1.name = 'harry'
print(s1.name)
# del s1.name
# print(s1.name)
# del s1

class Animal:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"hello {self.name}")
a = Animal("Lion")
a.greet()
        