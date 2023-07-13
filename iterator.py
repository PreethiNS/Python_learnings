l = [1,2,3,4]
# my_iter = iter(l)
# print(next(my_iter))
# print(next(my_iter))
# print(my_iter.__next__())
# print(my_iter.__next__())
# print(my_iter.__next__())

# iterable_val = "Geeks"
# iterable_obj = iter(iterable_val)
# while True:
#     try:
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
#         break

# list1 = [4,5,6,7]
# for i in list1:
#     print(i)

# class addsix:
#     def __init__(self,max=0):
#         self.max = max
#     def __iter__(self):
#         self.n =0
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result= self.n + 6
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
        
# number = addsix(9)
# i = iter(number)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# class MyNumbers:
#     def __iter__(self):
#         self.a= 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x= self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration
# mynum = MyNumbers()
# myiter = iter(mynum)

# for x in myiter:
#     print(x)

