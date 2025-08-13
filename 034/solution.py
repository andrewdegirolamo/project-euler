import math

def digit_factorial_checker(x):
    digits = [int(digit) for digit in str(x)]
    sum = 0
    for i in range(len(digits)):
        sum += math.factorial(digits[i])
    if sum == x:
        return True
    else:
        return False

print(digit_factorial_checker(144))


def full_solution(x):
    answer = 0
    for i in range(3,x+1):
        if(digit_factorial_checker(i)):
            answer += i
    return answer

print(full_solution(100000))