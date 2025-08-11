import math

primes = []
util_number = 2

def is_prime(x):
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if (x % i) == 0:
            return False
    return True

while (len(primes) < 100001):
    if is_prime(util_number):
        primes.append(util_number)
    util_number += 1

print(primes[10000])


