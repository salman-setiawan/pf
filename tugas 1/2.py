test = 5

def triangular(n):
    l = [i + 1 for i in range(n)]
    return sum(l)
    
print(triangular(test))