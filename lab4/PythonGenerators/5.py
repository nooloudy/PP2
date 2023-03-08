def GeneratorReverse(n):
    value = n
    while value >= 0:
        yield value
        value-=1
n = int(input())
for value in GeneratorReverse(n):
    print(value)