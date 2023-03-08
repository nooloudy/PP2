import os

path = "C://Users//GTA//Desktop//Python//lab6//directory and files//3//file.txt"

if os.path.exists(path):
    file_name = os.path.basename(path)
    print(file_name)
else:
    print("This file in puth does not exist")

#This code print name of file 
#for example: This path exists and my output will be file.txt

if os.path.exists(path):
    print(path)
else:
    print("This file it puth does not exist")
    
#A this code print all puth if file exists 