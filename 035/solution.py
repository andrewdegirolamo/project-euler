import math


def is_prime(x):
    if (x <= 1):
        return False
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if (x % i) == 0:
            return False
    return True

def find_all_primes(x):
    global all_primes
    all_primes = []
    for i in range(2,x):
        if(is_prime(i)):
            all_primes.append(i)
    return all_primes

all_primes = find_all_primes(1000000)

def rotater_checker(x):
    for r in range(len(str(x))):
        stringed = str(x)
        if(int(stringed[r:]+ stringed[:r]) not in all_primes):
            return False
    return True

def all_checks():
    answer = 0
    for i in range(len(all_primes)):
        if(rotater_checker(all_primes[i])):
            answer += 1
            print(i)
            print(len(all_primes))
    return answer

print(all_checks())
    

    
            

