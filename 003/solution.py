def prime_factors(x):
    factors = []
    factor = 2
    while (x > 1):
        if (x % factor == 0):
            factors.append(factor)
            x = x/factor
        else:
            factor += 1
    return factors

factors = prime_factors(600851475143)

print(factors)
print(max(factors))
