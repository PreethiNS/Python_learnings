#Implicit
print(62*2.5)
print(2**4)

import math
print(math.pi)

import random
print(random.random())

#string
a = "INDIA"
print(a[::-1])
print(a[0])
print(a[-1])
print(a[1:])
print(a + 'xyz')
print(a*3)
a= a.replace("IA","XYZ")
print(a)


#List
l1 = [101,"america",2.05]
print(l1)
print(l1[::-1])
print(len(l1))
print(l1[1])
print(l1[:-1])
l1.append("USA")
print(l1)
l1.pop(3)
print(l1)
l1.reverse()
print(l1)

#Dict
dict1 = {
    1:"Tiger",
    2:"Lion",
    3:"Mouse",
}
print(dict1)
print(dict1.keys())
print(dict1.values())
dict1[4] = "Cat"
print(dict1)

#Tuple objects
t1 = (1,2,3,4)
print(len(t1))
t2 = (5,6)
print(t1+t2)
print(t2[0])

#File
f1 = open("simple.txt",'w')
f1.write("Hello simplilearn\n")
f1.write("welcome to python programming\n")
f1.close()

#set
s= set("INDIA")
s1 = set(["U","S","A"])
print(s,s1)
print(s&s1)
a=7
b=2.0
r = a+b
print(r)


#explicit
#int(),float(),ord(),hex(),oct(),tuple(),set(),list(),dict(),str(),complex().chr()
a= 7
b= 2.0
r = int(a+b)
print(r)
#string and int addition not possible

s= "INDIA"
ts= tuple(s)
print(ts)
print(list(s))

t= ("john","merry")
print(list(t))

a=10
b= bin(a)
c=hex(a)
d=oct(a)
print(b,c,d)

n1 = 76
print(chr(n1))
print(chr(65))

s= 'A'
print(ord(s))

#operations: +, -,*,/,//,**,%
import fractions
print(fractions.Fraction(1,3))

x= -9.8
print(abs(x))

print(math.e)
print(math.exp(10))
print(math.log10(100))
print(math.factorial(6))
print(math.sqrt(25))
print(max(1,3,4,5))
print(min(2,3,4,5))
print(math.ceil(23.5))
print(math.floor(23.5))
print(math.pow(2,6))

import random
print(random.randrange(10,20))
x= [1,2,3,4,5]
print(random.choice(x))


