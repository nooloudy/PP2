def GeneratorSquare(a,b):
    result = (value * value for value in range(a,b))



a = int(input())
b = int(input())

for value in GeneratorSquare(a,b):
    print(value)
    
#result = (value * value for value in range(a,b))
#for i in result:
 #   print(i)