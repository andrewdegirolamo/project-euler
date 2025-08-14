import math

def double_squares(x):
    doubled = []
    for i in range(1,x):
        doubled.append(2 * (i ** 2))
    return doubled

def primes_less_than(x):
    if x <= 2:
        return []
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False 

    for i in range(2, math.isqrt(x) + 1):
        if(is_prime[i]):
            for a in range(i*i, x, i):
                is_prime[a] = False
    return [i for i in range(x) if is_prime[i]]

def odd_composite_finder(x):
    inverse = []
    for i in range(1, (x // 2 + 1)):
        inverse.append(i*2)
    inverse.extend(primes_less_than(x))
    inverse.append(1)
    odd_composites = []
    for i in range(1, x+1):
        if(i not in inverse):
            odd_composites.append(i)
    return odd_composites




all_double_squares = double_squares(10000)

all_comps = odd_composite_finder(10000)

all_primes = primes_less_than(10000)

found = False
counter = 0
while found == False:
    active_composite = all_comps[counter]
    for i in range(len(all_double_squares)):
        if ((active_composite - all_double_squares[i]) in all_primes):
            counter += 1
            break
    else:
        found = True
        print(all_comps[counter]) 
