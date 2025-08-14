import itertools
import math

numbers = [1,2,3,4,5,6,7]
pandies = []
for n in itertools.permutations(numbers):
    intify = list(map(str, n))
    joined = int(''.join(intify))
    pandies.append(joined)

def is_prime(x):
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if (x % i) == 0:
            return False
    return True


found = False
answer = 0
while found != True:
    if(is_prime(pandies[-1])):
        found = True
        answer = pandies[-1]
    else:
        pandies.pop()
        


print(answer)



