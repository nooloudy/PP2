import re

def ToSnake(s):
    return re.sub("(?!^)(?=[A-Z])", '_', s).lower()

text = input()

res = ToSnake(text)

print(res)