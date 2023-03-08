import re
text = input()
match = re.split('[A-Z]', text)
print(match)
