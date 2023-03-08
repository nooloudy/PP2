import os

path = "C://Users//GTA//Desktop//Python//lab6//directory and files//2//text.txt"

exist = os.access(path, os.F_OK)
print("Exists:",exist)

read = os.access(path, os.R_OK)
print("Read:", read)

write = os.access(path, os.W_OK)
print("Write:", write)

executability = os.access(path, os.X_OK)
print("Executed:", executability)
