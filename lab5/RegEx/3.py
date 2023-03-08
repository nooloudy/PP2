import re

text = input()

pattern = r'[a-z]+_*[a-z]+'
match = re.search(pattern, text)

print(match)