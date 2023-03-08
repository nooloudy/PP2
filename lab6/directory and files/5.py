import os 

path  = "C://Users//GTA//Desktop//pp2//lab6//directory and files//5.txt"

file = open(path, "w")
items = ['apple', 'banana','orange']

for i in items:
    file.write(i+"\n")
file.close()


