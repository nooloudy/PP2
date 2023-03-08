import os
path  = "C://Users//GTA//Desktop//pp2//lab6//directory and files//direct.txt"
file = open(path, "r")
cnt = 0
Read = file.read()
List = Read.split("\n")
for item in List:
    if item:
        cnt+=1
print(cnt)

