import re


text = input()

pattern = r'[A-Z][a-z]+'
match = re.search(pattern, text)

print(match.group())