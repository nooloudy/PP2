import os

path =  "C://Users//GTA//Desktop//Python//lab6//w3school//demofile.txt"
f = open(path,"r")
print(f.read())

#We are just open the file and read what is there

f1 = open(path,"r")
print(f1.read(5))
#Here I have specified how many characters to print

f2 = open(path, "r")
print(f2.readline())
#Thanks to readline, I was just returning the first line
print(f2.readline())
#If I write readline again it returns me the following line
f3 = open(path,"r")
for item in f3:
    print(item)
#In this moment the program will return me all the line in this file

f4 = open(path,"r")
print(f4.readline())
f4.close()
#close the file when you done with it