import os

Delete_file = "delete.txt"

path = "C:\\Users\\GTA\\Desktop\\pp2\\lab6\\directory and files\\8"

location = os.path.join(path, Delete_file)

try:
    os.remove(path)
except:
    print("The specified file not found")
#if os.path.exists(path):
 #   if not os.path.join(path, Delete_file):
 #       print("The specified file not found")
 #   else:
  #      os.remove(os.path.join(path,Delete_file))
   
