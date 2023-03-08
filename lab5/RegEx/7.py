import re


text = input()

match = re.split('_', text)

for iter in match:
    print(iter, sep = '')
