# class Bikes:
#     def __init__(self,brandname,year):
#         self.brandname = brandname
#         self.year = year

# bike1 = Bikes("BMW",2021)
# bike2 = Bikes("ducati",2020)
# print(bike1.brandname,bike1.year)
# print(bike2.brandname,bike2.year)

# class Bikes:
#     def __init__(self,brandname,year):
#         self.brandname = brandname
#         self.year = year
#     def topspeed(self,topspeed):
#         return f"topspeed of Bike {self.brandname} is {topspeed}"
#     def type(self):
#         return f"{self.brandname} is geared bike"
# bike1 = Bikes("BMW",2000)
# print(bike1.topspeed(200))
# print(bike1.type())

#Inheritance
#single
# class Animal:
#     def sound(self):
#         print("Animal making sound")
# class Cat(Animal):
#     def meow(self):
#         print("cat meows")

# c = Cat()
# c.meow()
# c.sound()

# #multilevel
# class Animal:
#     def sound(self):
#         print("Animal making sound")
# class Cat(Animal):
#     def meow(self):
#         print("cat meows")
# class Catchild(Cat):
#     def eat(self):
#         print("Eating bread..")

# cc = Catchild()
# cc.eat()
# cc.meow()
# cc.sound()
# c = Cat()
# c.meow()
# c.sound()
# a = Animal()
# a.sound()

#hierarchical
# class Animal:
#     def eat(self):
#         print("eating bread...")
# class Dog(Animal):
#     def run(self):
#         print("running..")
# class Cat(Animal):
#     def catch(self):
#         print("Catching..")

# d= Dog()
# d.run()
# d.eat()

# c= Cat()
# c.catch()
# c.eat()

#Multiple
# class Mom:
#     def confidence(self):
#         print("mom is confident so Iam")
# class Dad:
#     def friendly(self):
#         print("dad id friendly so Iam")
# class child(Mom,Dad):
#     def unique(self):
#         print("i am unique")
# c = child()
# c.unique()
# c.friendly()
# c.confidence()

#Polymorphism
# class Parrot:
#     def fly(self):
#         print("Parrot can fly")
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")
#     def swim(self):
#         print("Penguin can swim")
# def flying_test(bird):
#     bird.fly()

# blu = Parrot()
# peg = Penguin()

# flying_test(blu)
# flying_test(peg)

#encapsulation
# class Cars:
#     def __init__(self):
#         self.__maxprice = 900000      #private attribute
#     def sell(self):
#         print(f"{self.__maxprice}")
#     def setMaxPrice(self,price):
#         self.__maxprice =price

# c = Cars()
# c.sell()
# c.__maxprice = 800000
# c.sell()

# c.setMaxPrice(80000)
# print(c.__maxprice)

#abstraction
# class Car:
#     def mileage(self):
#         pass

# class BMW(Car):
#     def mileage(self):
#         print("the mileage is 30kmph")
# class Jaguar(Car):
#     def mileage(Self):
#         print("The mileage is 25kmph")

# bmw = BMW()
# bmw.mileage()

# j= Jaguar()
# j.mileage()

#__init__()
# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname= lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
# s= Student("Pree","NS")
# s.printname()

# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname= lname
#     def printname(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
# s= Student("Pree","NS")
# s.printname()

#issubclass method
# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b
# class Derived(Calculation1,Calculation2):
#     def divide(self,a,b):
#         return a/b
# d= Derived()
# print(issubclass(Derived,Calculation2))
# print(issubclass(Calculation1,Calculation2))

#isinstance
class Calculation1:
    def Summation(self,a,b):
        return a+b
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d= Derived()
print(isinstance(d,Calculation2))
print(isinstance(d,Calculation2))
print(isinstance(d,Derived))

c= Calculation1()
print(isinstance(c,Derived))

