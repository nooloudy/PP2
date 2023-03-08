import os
#"a" - Append - will append to the end of the file

#"w" - Write - will overwrite any existing content

path = "C://Users//GTA//Desktop//Python//lab6//w3school//demofile2.txt"

test = open(path, "a")
test.write("Now the file has more content!")
test.close()

f = open(path, "r")
print(f.read())
