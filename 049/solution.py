import math

def primes_less_than(x):
    if x <= 2:
        return []
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False 

    for i in range(2, math.isqrt(x)):
        if(is_prime[i]):
            for a in range(i*i, x, i):
                is_prime[a] = False
    return [i for i in range(x) if is_prime[i]]


base_primes = primes_less_than(10000)
filtered = [p for p in base_primes if p >= 7660]

for p in range(len(filtered)):
    double_filtered = []
    if (filtered[p] - 3330 in base_primes and filtered[p] - 6660 in base_primes):
        if ("".join(sorted(str(filtered[p]))) == "".join(sorted(str(filtered[p]-3330))) == "".join(sorted(str(filtered[p]-6660)))):
            print(str(filtered[p]-6660) + str(filtered[p]-3330) + str(filtered[p]))







