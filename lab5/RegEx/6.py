import re

text = input()

match = re.sub('\s', ':', text)
match = re.sub('[.]', ':', match)
match = re.sub('[,]', ':', match)


print(match)