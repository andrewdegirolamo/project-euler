import math

def factorial_digit_sum(x):
    base_factorial = math.factorial(x)
    digits = [int(digit) for digit in (str(base_factorial))]
    return sum(digits)

print(factorial_digit_sum(100))
