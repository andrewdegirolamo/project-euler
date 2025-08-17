import math
import networkx as nx
import matplotlib.pyplot as plt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in [2, 7, 61]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def primes_less_than(x):
    if x <= 2:
        return []
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False

    for i in range(3, math.isqrt(x) + 1):
        if(is_prime[i]):
            for a in range(i*i, x, i):
                is_prime[a] = False
    return [i for i in range(x) if is_prime[i]]

primes = primes_less_than(10000)

def concatenator(a,b):
    return int(str(a) + str(b))

linked_primes = nx.Graph()

def concatenation_checker(a,b):
    if (is_prime(concatenator(a,b)) and is_prime(concatenator(b,a))):
        linked_primes.add_nodes_from([a,b])
        linked_primes.add_edge(a,b)

for a in range(0,len(primes)):
    for b in range(a + 1, len(primes)):
        concatenation_checker(primes[a],primes[b])

cliques = list(nx.find_cliques(linked_primes))

sets_of_5 = [clique for clique in cliques if len(clique) == 5]

sums = []
for i in range(len(sets_of_5)):
    sums.append(sum(sets_of_5[i]))

print(min(sums))




