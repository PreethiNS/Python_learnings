#lists
#append,insert,extend,index,remove,sort,reverse
l1 = [1,2,3,4,5]
print(sorted(l1,reverse= True))
print(l1)
l2= ["apple",[3,4,5],"orange"]
print(l2)
print(l2[1])
print(l2[1][2])
print(l1[-1])
print(l1[2:])
l1.append(9)
print(l1)
l1.extend([12,10,11])
print(l1)
del l1[0]
print(l1)
l1.remove(2)
print(l1)
print(l1.pop(1))
l2.clear()
print(l2)
l1.reverse()
print(l1)
print(l1.index(10))
print(l1.count(11))
l1.insert(1,13)
print(l1)

#Tuple
#index,slicing,concatenation,repetition,count
t1 = (1,2,3,4,1,2)
print(t1)
t2 = ("apple",)        #dont provide comma considered as string put comma for tuple which has single element
print(t1[1:])
print(t1[3])
print(t1[-1])
print(("repeat",)*3)
print(t1.count(1))
print(t1+t2)
print(t1.index(1))
y = list(t1)
y.append(100)
print(tuple(y))
for x in t1:
    print(x)

#dict
#ordered,cannot use index,various typess of ele,mutable,doesn't allow duplicate
#clear(),get(key),keys(),values(),pop(key),popitem()
d= {
    1: "apple",
    2: "Orange",
    3: "Banana",
    4: "Kiwi"
}
print(d)
print(d[1])
print(d.get(2))
print(d.pop(3))
print(d.keys())
print(len(d))
print(d.values())
print(sorted(d))
d.update({2:'watermelon'})
print(d)
d.update({5:'xyz'})
print(d)
d.popitem()
print(d)

for x in d:
    print(d[x])

for x,y in d.items():
    print(x,y)

d2 = d.copy()
print(d2)

d2.clear()
print(d2)

del d[1]
print(d)