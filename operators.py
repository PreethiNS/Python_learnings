#arithmetic,Comparision,Assignemnt,Logical,Bitwise,Identity,Membership
#identity: is, is not
#Membership : in ,not in
x= 505
y= 500 + 5
print(x is y)
print(id(x),id(y))
x= 100
y=200
print(x is y)
a= [1,2,3,4]
b=[1,2,3,4]
c=a
print(a is c)
print(a is not b)

a= [1,2,3,4,5]
b=[8,9,6,7]
print(5 in a)
print(4 in b)
y= {'a':'India','b':'USA'}
print('a' in y)         
print('India' in y)       #membership not supported on values, only on keys

