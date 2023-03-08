import re

text = input()

match = re.split('[A-Z]', text)

for iter in match:
    print(iter, ' ')
