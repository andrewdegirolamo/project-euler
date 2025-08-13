import math

answer = 0

def half_divisor_finder(x):
    divisor_list = []
    for i in range(1,(int(math.sqrt(x)))+1):
        if(x % i == 0):
            divisor_list.append(i)
    return divisor_list

def pandigital_checker(x):
    global answer
    divisors = half_divisor_finder(x)
    is_pandigital = False
    for i in range(len(divisors)):
        other_number = x // divisors[i]
        checker = str(x) + str(divisors[i]) + str(other_number)
        sorted_checker = int("".join(sorted(checker)))
        if (sorted_checker == 123456789):
            is_pandigital = True
    if(is_pandigital):
        answer += x

for i in range (1,10000):
    pandigital_checker(i)

print(answer)