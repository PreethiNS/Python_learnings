# try:  
#     a= int(input())
#     b= int(input())
#     c= a/b
#     print(c)
# except:
#     print("can't divide by zero")

# a= 70
# b=0
# try:
#     print(a/b)
#     print("New Line")
# except ZeroDivisionError:
#     print("Do not divide number by zero")
# print("completed")

# a=70
# b=9
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero")  
# print("completed")    

# try:
#     a= int(input("enter a: "))
#     b= int(input("enter b: "))
#     c=a/b
#     print(c)
# except Exception:
#     print("can't divide by zero")
#     print(Exception)
# else:
#     print("Simple")

# a= 10
# b=0
# try:
#     print(a/b)
# except Exception as a:
#     print("cannot divide by zero",a)
# print("completed")

# a= 10
# b=0
# try:
#     print(a/z)
# except Exception as a:
#     print("cannot divide by zero",a)
# except NameError as b:
#     print(b)
# print("completed")

# try:
#     a=5
#     b=0
#     print(a/b)
# except TypeError:
#     print("Unsupported operation")
# except ZeroDivisionError:
#     print("Division by zero not allowed")

# x= -15
# if x<0:
#     raise Exception("sorry,no numbers below zero")

import sys
assert("linux" in sys.platform),"compatible with linux only"