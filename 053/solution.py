import math

def factorialize(n,r):
    return math.factorial(n) / (math.factorial(r) * math.factorial((n-r)))
        
counter = 0
for n in range(1,101):
    for r in range(1,n+1):
        if(factorialize(n,r)> 1000000):
            counter += 1
print(counter)