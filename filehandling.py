f= open("sample.txt","w")
f.write("hey you are stronger than you think\n")
f.close()
s= open("sample.txt","r")
print(s.read())
s.close()
s= open("sample.txt","r")
print(s.read(7))
s.close()
f= open("sample.txt","a")
f.write("you can do it")
f.close()
s= open("sample.txt","r")
print(s.readline())
s.close()
s= open("sample.txt","r")
print(s.readlines())
s.close()

import os 
os.remove("sample.txt")
