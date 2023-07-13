# #local scope
# def fun():
#     s = "Simple"
#     print(s)
# fun()

# #try to access it outside function
# def func1():
#     s1 = "simple"
#     print(s1)
# func1()
# #print(s1)  - not accessible

# #enclosed scope -function inside another function
# def func():
#     s2 = "simple"
#     def inner_func():
#         print(s2)
#     inner_func()

# func()

# msg = "This is a global scope message"
# def outer_func():
#     msg = "this is an outer variable"
#     def inner_func():
#         #msg = "inner function variable"
#         nonlocal msg 
#         print(msg)
#     inner_func()
# outer_func()
# print(msg)

#global scope
# x= 50
# def my_func():
#     print(x)
# my_func()

# msg1 = "hello"
# def func1():
#     global msg1
#     #msg1 = "world"
#     print(msg1)
# func1()

# def func3():
#     global s
#     s= "simple"
# func3()
# print(s)

# a1 = 'india'
# def my_country():
#     global a1
#     a1 = "France"
# my_country()
# print(a1)

#Built-in scope
from math import pi
# pi = "global pi var"
def func():
    # pi = "This is outer pi var"
    def inner():
        # pi = "This is inner pi var"
        print(pi)
    inner()
func()


