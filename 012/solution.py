import math

base = 1
additive = 2

def divisor_checker(x):
    if x <= 0:
        return 0
    divisors = 0
    sqrt_x = int(math.sqrt(x))
    for i in range(1, sqrt_x +1):
        if x % i == 0:
            if i * i == x:
                divisors += 1
            else:
                divisors += 2
    return divisors

while ((divisor_checker(base)) < 500):
    base = base + additive
    additive += 1
    

print(base)