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

all_primes  = primes_less_than(1000000)
utility_prime = primes_less_than(1000000)

tester_primes = primes_less_than(10000)



def create_consecutive_primes(maxi):
    prime_set = set(all_primes)
    max_prime = 0
    max_length = 0
    
    for start in range(len(utility_prime)):
        current_sum = 0
        for length in range(start, len(utility_prime)):
            current_sum += utility_prime[length]
            if current_sum >= maxi:
                break
            if current_sum in prime_set and (length - start + 1) > max_length:
                max_prime = current_sum
                max_length = length - start + 1
    
    return max_prime


print(create_consecutive_primes(1000000))
