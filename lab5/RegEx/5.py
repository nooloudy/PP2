import re



text = input()

pattern = r'a.*b'
match = re.search(pattern, text)

print(match)