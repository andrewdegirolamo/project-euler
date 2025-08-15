def prime_factors(x):
    if x == 1:
        return [1]
    n = 2
    factors = []
    while n**2 <= x:
        if x % n == 0:
            factors.append(n)
            x //= n
        else:
            n+=1
    if x > 1:
        factors.append(x)
    return list(set(factors))

streak = 0
counter = 1000
while streak != 4:
    if(len(prime_factors(counter)) == 4):
        streak +=1
        counter +=1
    else:
        streak = 0
        counter +=1

print(counter - 4)