palindromes = []

def palindrome_checker(x):
    if str(x) == (str(x))[::-1]:
        return True
    else:
        return False
    
for i in range (1000):
    for x in range (1000):
        if palindrome_checker(i * x):
            palindromes.append(i * x)

print(max(palindromes))