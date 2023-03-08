import re

txt = input()

a = re.findall("abb*" , txt)

print(a)