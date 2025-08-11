import math

answer = 0

def is_prime(x):
    if (x <= 1):
        return False
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if (x % i) == 0:
            return False
    return True

for i in range(2000000):
    if (is_prime(i)):
        answer += i

print(answer)