# def my_gen():
#     n =1
#     print("this is printed first")
#     yield n

#     n += 1
#     print("This is printed second")
#     yield n

#     n+=1
#     print("this is third")
#     yield n

# for i in my_gen():
#     print(i)

# def my_gen1():
#     print("first one")
#     yield 10

#     #return

#     print("Second one")
#     yield 20

# m = my_gen1()
# next(m)
# next(m)
# for i in my_gen1():
#     print(i)

# l1 = [1,2,3,4]
# list2 = [x**2 for x in l1]
# gen = (x**2 for x in l1)
# print(list2)
# print(gen)
# for i in gen:
#     print(i)

#infinite value generation
# def all_even():
#     n = 0
#     while True:
#         yield n 
#         n += 2
# for item in all_even():
#     print(item)

#pipelining with generators
def fib(nums):
    x,y = 0,1
    for i in range(nums):
        x, y = y , x+y
        yield x 
def square(nums):
    for num in nums:
        yield num ** 2

print(sum(square(fib(10))))
