import os
import shutil
path_1 = "C://Users//GTA//Desktop//pp2//lab6//directory and files//7//first.txt"
path_2 = "C://Users//GTA//Desktop//pp2//lab6//directory and files//7//second.txt"

with open(path_1, "r") as first, open (path_2, 'w') as second:
    for item in first:
        second.write(item)

first.close()
second.close()
