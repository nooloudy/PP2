word = input() 
 
def isPal(word): 
 
    return True if word[::-1] == word else False 
 
print(isPal(word)) 