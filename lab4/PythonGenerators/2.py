




def mysecond_generator(n):
    value = 0
    while value <= n:
        yield value
        value+=1
m = int(input())
for value in mysecond_generator(m):
    if value % 2 == 0:
        print(value,end = ' ' )
