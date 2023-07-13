#built-in functions
#abs
# num = abs(98.5)
# print(num)
# num = abs(-98.5)
# print(num)
# #len
# l1 = [1,2,3,4,5]
# print(len(l1))
# #all:if any value in the list 0 then it will result False otherwise True
# my_list = [1,2,3,4,5,0,0]
# x= all(my_list)
# print(x)
# #sum
# s= sum([1,2,3,4,5,10])
# s1= sum((7,8,9))
# print(s,s1)
# #max and min
# mx = max(1,2,3,9,5,4)
# mi= min(1,2,5,7,3,10)
# print(mx,mi)
# #iter()
# mylist = iter([1,2,3,4,5])
# x= next(mylist)
# print(x)
# x= next(mylist)
# print(x)
# #pow
# print(pow(2,3))
# #range()
# x= range(6)
# for n in x:
#     print(n)
# x= range(40,50,2)
# for n in x:
#     print(n)
# #round
# x= round(8.625467,2)
# print(x)
# #sorted
# a =[10,9,1,2,3,7]
# print(sorted(a))
# print(sorted(a,reverse=True))
# #slice
# a= (1,2,3,4,5)
# x= slice(3)
# print(a[x])

#user-defined
# def func1():
#     print("Hello world")
# func1()

# def hello():
#     name = input("enter your name: ")
#     print(f"Hello {name}")
# hello()

# def ft_to_cm(ft):
#     cent = ft * 30.48
#     return cent 
# ce =ft_to_cm(6)
# print(ce)

# def add(x,y):
#     return x+y
# print(add(3,4))

# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -(-x)
    
# print(absolute(56))
# print(absolute(-56))

# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
    
# print(factorial(5))

#default arg
# def welcome(name="Paul"):
#     print(f"hello {name}")
# welcome()

# def welcome(name="Paul"):
#     print(f"hello {name}")
# welcome("Pree")

#multiple arg
# def message(name1,name2,name3):
#     print(f"hello {name1} {name2} {name3}")
# message("x","y","z")

#scope
# def func1():
#     z= 7
#     print(z)
# #print(z)     -since its local scope not able to access the value
# func1()

# z=7
# def func2():
#     print(z)
# print(f"outside z:{z}")
# func2()

# z=7
# def func3():
#     z= z+1         #this will throw an error
#     print(z)

# func3()

# z=7
# def func3():
#     global z
#     z= z+1
#     print(z)

# func3()

# def welcome(*names):
#     print(f"hello {names[0]} {names[1]}")

# welcome('xyz','abc','stu')

# pi = 3.14
# def circleArea(r):
#     return pi*r*r
# def sphereArea(r):
#     return 4*pi*r*r
# def main():
#     print(f"circle {circleArea(15)}")
#     print(f"sphere {sphereArea(8)}")

# main()

#lambda
# add = lambda a,b: a+b
# print(add(2,3))

# add = lambda x: x+100
# print(add(50))

# print((lambda a,b : a*b)(15,5))

# product = lambda x,y,z: x*y*z
# print(product(z=5,x=10,y=4))

# add =lambda x,y=15,z=24: x+y+z
# print(add(10))

# addition = lambda *args: sum(args)
# print(addition(20,30,40,10))

# higher_ord_fun = lambda x,fun: x+ fun(x)
# print(higher_ord_fun(20,lambda x:x*x))

# print((lambda x : (x%2 and 'odd' or 'even'))(30))

# sub_string = lambda string: string in "Welocme to python Tutorial"
# print(sub_string('Java'))
# print(sub_string('python'))

# num = [10,40,56,27,33]
# greater = list(filter(lambda num: num>30,num))
# print(greater)

# list1 = [10,40,30,50,60]
# divide = list(filter(lambda x: (x%4==0),list1))
# print(divide)

# list2= [10,20,30,40]
# double = list(map(lambda x: x*2,list2))
# print(double)

# list1= [1,2,3,4,5]
# cube = list(map(lambda x: pow(x,3),list1))
# print(cube)

# from functools import reduce
# list4 = [1,2,3,4,5]
# sum = reduce((lambda x,y:x*y),list4)
# print(sum)

def quadratic(a,b,c):
    return lambda x:a*x**2 + b*x +c
f= quadratic(1,2,3)
print(f(1))








