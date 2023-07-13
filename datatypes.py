#Numeric
num = 7
print(type(num))
print(num,"is of type",type(num))
 
num = 10.8
print(type(num))

num= -10.8
print(type(num))

num= 8+6j
print(type(num))
print(num.real,num.imag)

num = 7.8
print(int(num))
num= -90.5
print(type(num),int(num))

b= 7
c=float(b)
print(c)

#Boolean
r= True
print(type(r))
num=-90.5
c= 8
print(num>c)

#strings
str1 = "Python programming"
str2 = "simple"
print(type(str1))
print(str1[5])
print(str2[-4])
print(str1[0:5])
print(str1.find('m'))

#sequence
#list
split1 = "This,is,Orange"
l1 = split1.split(",")
print(l1)
print(type(split1))
print(type(l1))

l2 = ['a',1,2,3,'India']
print(l2)
l3= [4,5,6]
print(l2+l3)

#Tuple
t1 =(1,2,3,4,"India")
print(t1)
t2 =(4,5,6)
print(t1+t2)
print(t1*2)

#Map:dict
d = {
    1:"Lion",
    2:"Tiger",
    3:"Dog",
}
print(d,type(d),len(d))

#Set
s1= {1,2,3,4,5,4,5}
print(s1,type(s1))
s2 = {7,8,9,"India",1}
print(s1 | s2)
print(s1 & s2)
print(s1-s2)
print(s2-s1)

#Range
x = range(4)
print(x)
print(*x)

#Binary Data types
x= b"Hello world"
print(x,type(x))
print(x[4])

#conversion
s = "Messi is from Argentina"
l = list(s)
print(l)

l1 = [1,2,3,4,5,1,2,3]
s1 = set(l1)
print(s1)

#string continuation
#double quotes,sing quote, triple quote -multiline strings/doc strings
#forward index, reverse index
str1 = 'Hi Sam'
print(str1)
str2 = "Hello angela!"
print(str2)
str3 = """
Hii everyone
today we will learn about 
strings in python
"""
print(str3)
str1 = "Simple"
print(str1[0])
print(str1[0::2])
print(str1[::-1])
print(str1[-2:])
print(str1[:-2])
# str1[3] ='o'                    #does not support item assignment
# print(str1)
# str2 = "python"
# del str2
# print(str2)

#string operations
str1 = "python"
str2 ="pragramming"
print(str1*3)
print(str1+str1)
print(str1+str2)
print('w' in str1)
print('p' in str1)
print('ra' in str2)
print(r'C://python3.7')

#format
print("{} and {} both are best friends".format("xyz","pqr"))
print("{1} and {0} both are best friends".format("xyz","pqr"))
print("{a} and {b} both are best friends".format(a="xyz",b="pqr"))
name = "Angela"
salary = 100000
print("Her name is %s\nHer salary is%d"%(name,salary))

str1 = "simple"
str2 = str1.capitalize()
print(str2)
str3 = "SIMPLE"
print(str3.casefold())
str4 = "sImPLIearn"
print(str4.upper())
print(str4.lower())
str5 = "abc xyz pqr"
print(str5.title())
print(str5.count('c'))
str5=str5.replace("abc","stu")
print(str5)

#split 
str6 = "hey-you-are-amazing"
print(str6.split("-"))

