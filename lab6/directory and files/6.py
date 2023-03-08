import os
import string
path = "C:\\Users\\GTA\\Desktop\\pp2\\lab6\\directory and files\\Alphabet"

if not os.path.exists(path):
     file = os.makedirs(path)

for i in string.ascii_uppercase:
    file = open(i+ ".txt" , "w")
    file.writelines(i)
    file.close()