import os

path = "C://Users//GTA//Desktop//Python//lab6//directory and files//1"
directories = []
files = []
both= []
# dir_of_list = os.listdir(file)

# print(dir_of_list)
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path,item)):
        directories.append(item)
    elif os.path.isfile(os.path.join(path,item)):
        files.append(item)
        

for item in os.listdir(path):
    if os.path.isdir(path)or os.path.isfile(path):
        both.append(item)

print('directories:')
print(directories)

print('files:')
print(files)

print('directories and files:')
print(both)
    