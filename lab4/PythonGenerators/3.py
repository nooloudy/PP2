n = int(input())
a = (value % 3 == 0 and value % 4 == 0 for value in range(n))
for i in a:
    print(i)
    