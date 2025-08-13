import math

optimal = []
max_checker = 0

def is_prime(x):
    if (x < 2):
        return False
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if (x % i) == 0:
            return False
    return True

for a in range(-1000, 1000):
    for b in range(-1001, 1001):
        global checker, prime
        prime = True
        checker = 0
        while prime == True:
            equation = checker ** 2 + (a * checker) + b
            if(is_prime(equation)):
                checker += 1
            else:
                prime = False
            if checker > max_checker:
                optimal = [a,b]
                max_checker = checker

print(math.prod(optimal))