import cmath

import string

def String(str):
    lower = 0
    upper = 0
    
    for i in str:
        if (i>='a' and i<='z'):
            lower+=1
        elif (i>= 'A' and i<='Z'):
            upper+=1
    print("Number of upper case : ", upper)
    print("Number of lower case : ", lower)
String("Nurlybek")

def Str(s):
    lower_list = 0
    upper_list = 0
    
    for char in s:
        if (char.islower()):
            lower_list+=1
        elif (char.isupper()):
            upper_list+=1
        else:
            pass
    print("Upper case : ", upper_list)
    print("Lower case : ", lower_list)
Str('Nurlybek')