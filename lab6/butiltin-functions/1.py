import math
#Nurlybek Krasavchik
def multiply_list(numbers):
    cnt = 1
    for number in numbers:
        cnt*= number
    return cnt
print(multiply_list((8,1,2,3,4)))

#in built in function

def multiply(numbers):
    result = math.prod(numbers,start = 1)
    return result

print(multiply((8,1,2,3,4)))