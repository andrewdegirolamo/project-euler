def prime_factor(num):
    if num == 1:
        return []
    n = 2
    factors = []
    while n**2 <= num:
        if num % n == 0:
            factors.append(n)
            num //= n
        else:
            n+=1
    if num > 1:
        factors.append(num)
    return list(set(factors))

def euler_totient(n):
    value = n
    for p in prime_factor(n):
        value -= value // p
    return value

current_max = 0
current_best = 0
for i in range (1,1000001):
    if (i/euler_totient(i) > current_max):
        current_max = i/euler_totient(i)
        current_best = i
        print(i)
print(i)