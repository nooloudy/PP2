import os 
path  ="C://Users//GTA//Desktop//Python//lab6//w3school//Delete//dsad.txt"

if os.path.exists(path):
    os.remove(path)
    print("File succesfully delected")
else:
    print("This file does not exists")
