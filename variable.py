a= 50
print(a)
print(type(a))
print(id(a))

a= 100
print(id(a))

#multiple values assigned to variables in single line
(x,y,z)= 50,168.6,"simple"
print(x,y,z)
print(type(z))

x=y=z=10
print(x,y,z)

(x,y,z)= 10,10,10
print(x,y,z)

#Rules for variable naming
abc = 100
print(abc)
a102 = "India"
print(a102)
_123 = 70.5
print(_123)
_dog="puppy"
print(_dog)
_name_age= 36
print(_name_age)
# 4name = 'gilly'    -error:do not start with number
# print(4name)
# @age = 40          -error:special character
# print(@age)
car,Car,CAR="BMW","XYZ","PQR"   #case sensitive
print(car,Car,CAR)
#break = 123          reserve keywords not used as variable name

#Operations
a= 100
b=200
result = a+b
print(result)
print(a-b,a*b,a/b,b//a,a%b)

country = "India"
print(country[3])
print(country[:3])

cars = ["xyz","pqr","stu"]
print(cars)
x,y,z= cars
print(x,y,z)

x= "simple"
print("welcome to "+ x)

# x= 20
# y= "simple"
# print(x+y)           #cannot concatenate int and string

#camelCase
myName = "preethi"
print(myName)
#PascalCase
MyName = "harry"
print(MyName)
#snake_case
my_name = "xyz"
print(my_name)