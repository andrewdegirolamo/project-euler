import math

def digitize(x):
    return list(map(int, str(x)))

def factorialize(x):
    digits = digitize(x)
    sum = 0
    for i in range(len(digits)):
        sum += math.factorial(digits[i])
    return sum

def loop_finder(x):
    factors = [x]
    looped = False
    while looped == False:
        next_number = factorialize(factors[-1])
        if (next_number in factors):
            looped = True
        elif (len(factors) > 60):
            return 61
        else:
            factors.append(next_number)  
    return len(factors)

answer = 0
for i in range(1,1000000):
    if(loop_finder(i) == 60):
        answer += 1
print(answer)