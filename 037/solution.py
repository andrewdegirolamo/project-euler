import math

def sieve(n):
    is_prime = bytearray(b"\x01") * n
    if n > 0: is_prime[0] = 0
    if n > 1: is_prime[1] = 0
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            start = i * i
            is_prime[start:n:i] = b"\x00" * (((n - 1 - start) // i) + 1)
    primes = [i for i, v in enumerate(is_prime) if v]
    return is_prime, primes

def right_trunc_prime(n, is_prime):
    while n > 0:
        if not is_prime[n]:
            return False
        n //= 10
    return True  

def left_trunc_prime(n, is_prime):
    m = 10 ** (len(str(n)) - 1)
    while m > 0:
        if not is_prime[n]:
            return False
        n %= m        
        m //= 10
    return True

def is_trunc_prime(n, is_prime):
    s = str(n)
    if any(d in s for d in "0245685"):
        return False
    return right_trunc_prime(n, is_prime) and left_trunc_prime(n, is_prime)

def find_truncs(limit):
    is_prime, primes = sieve(limit)
    truncs = [p for p in primes if p >= 10 and is_trunc_prime(p, is_prime)]
    return truncs

if __name__ == "__main__":
    truncs = find_truncs(1_000_000)
    print(sum(truncs))
