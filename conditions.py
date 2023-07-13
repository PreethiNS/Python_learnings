# total = int(input("Enter the amount for item: "))
# state = input("enter the state name in USA: ")
# if state == "Texas":
#     if total <= 150:
#         print("Shipping cost in Texas is $30")
#     elif total > 150 and total <=250:
#         print("Shipping cost in Texas is $20")
#     else:
#         print("Shipping cost in Texas is $5")
# elif state == "Florida":
#     if total <= 150:
#         print("Shipping cost in Florida is $45")
#     elif total >150 and total <= 250:
#         print("Shipping cost in Florida is $35")
#     else:
#         print("Shipping cost in Florida is $10")
# else:
#     print("enter valid state")

#loops
# i=0
# while i<10:
#     print(i,end='#')
#     i +=1

# count = 0
# while count <= 5:
#     print("The condition is True")
#     count += 1
# print("end of loop")

# while True:
#     print("Please type your name.")
#     name = input()
#     if name == "Gilly":
#         break
# print("Thank you")

#lCM of 4 and 7
# x = 0
# while True:
#     x +=1
#     if not(x%4 or x%7):  
#         break
# print(x,'is divisible by 4 and 7')

# i=0
# while i < 10:
#     i +=1
#     if i==6:
#         continue
#     print(i)

# #while and else
# i=1
# while i<5:
#     print(i)
#     i += 1
# else:
#     print("i is not less than 5")

# a= [1,2,3,4,5]
# while a:
#     print(a.pop())
# else:
#     print("there are no elements left in list")

# #avg of positive numbers
# num =0
# count = 0
# sum = 0

# while num >=0:
#     num = int(input('enter any positive number'))
#     if num > 0:
#         count +=1
#         sum += num
# avg = sum /count
# print("total: ",sum)
# print("avg: ",avg)

# import random
# n = random.randint(1,100)
# print(n)

# guess = int(input("enetr a number: "))
# while n <=100:
#     if guess < n:
#         print("guess is low")
#         guess = int(input("enetr a number: "))
#     elif guess > n:
#         print("guess is high")
#         guess = int(input("enetr a number: "))
#     else:
#         print("guess is correct")
#         break

#for loop- over the lists, tuples, dict, or strings
#uses range() function
# s= 'simple'
# for i in s:
#     print(i,end="*")
# print()

# l=[1,2,3,4,5]
# for i in l:
#     print(i,end=" ")
# print()

# sum =0
# for i in l:
#     sum +=i
# avg = sum/len(l)
# print(avg)

# t= (1,2,3,4,5)
# for i in t:
#     print(i)

# for i in range(1,100,2):
#     print(i)

# num = int(input("enter a number: "))
# for i in range(1,11):
#     result = num * i
#     print(f"{num}*{i}={result}")

# num = [1,2,3,4,5]
# for i in range(len(num)):
#     print(num[i])

# companies = ["google","Apple","PWC"]
# for i in companies:
#     print(i)
#     for letter in i:
#         print(letter)

#for-else
# for i in range(0,10,3):
#     print(i)
# else:
#     print("The loop has completed execution")

#break
# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)

# for i in range(1,10):
#     if i == 6:
#         continue
#     print(i)

#dict
# player_name = 'xyz'
# d = {
#     'Edison': 14,
#     'Bernat': 3,
#     'Carmelo':7,
# }
# for player in d:
#     if player == player_name:
#         print(d[player])
#         break
# else:
#     print("No player with that name found")

# #cube of number
# num = [2,3,4,5,7]
# cube = []
# for i in num:
#     cube.append(i**3)
# print(cube)

#pattern printing
# n = int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(0,i+1):
#         print("*", end="")
#     print()

#looping techniques
# num = [2,5,10,4,50,9,5,4]
# for item in sorted(set(num),reverse=True):
#     print(item)

# s = ["Messi","Ronaldo","Salah","harry"]
# for i in sorted(s,reverse= True):
#     print(i)

# d = {
#     'f':1,
#     'b':4,
#     'a':3,
#     'e':9
# }
# for key,val in sorted(d.items()):
#     print(key,val)

# players = ['Messi','Ronaldo','Salah','Harry']
# for i in reversed(players):
#     print(i)

# animals = [{"name":"Dog","age":11},{"name":"Lion","age":30}]
# for animal in filter(lambda i:i["age"]%2==0, animals):
#     print(animal)

# country = ['India','Usa','Canada']
# while country:
#     print(country.pop())

# print(country)

# num = 10
# while num>0:num = num-1;print(num)

# while True:
#     num = int(input("enter an integer: "))
#     print(num)

#enumerate
# for i in enumerate(['The','brown','fox','jumped']):
#     print(i)

# for key,val in enumerate(['The','brown','fox','jumped']):
#     print(key,val)

# company = 'simple'
# for i,j in enumerate(company):
#     print(i,j)

# company = 'simple'
# for i in enumerate(company,start=10):
#     print(i)

#zip
# first = ['Lion','Tiger','Dog']
# last = ['xyz','pqr','stu']
# num = [1,2,3,4,5]
# for i in zip(first,last,num):
#     print(i)

# from itertools import zip_longest
# first = ['Lion','Tiger','Dog','Lion']
# last = ['xyz','pqr','stu']
# for i in zip_longest(first,last):
#     print(i)

# from itertools import zip_longest
# first = ['Lion','Tiger','Dog','Lion']
# last = ['xyz','pqr','stu']
# for i in zip_longest(first,last,fillvalue="NA"):
#     print(i)









        