answer = 0
def binary_finder(x):
    input = x
    base_2 = []
    while input != 0:
        base_2.append(input % 2)
        input = input // 2
    return (("".join(str(bit) for bit in base_2))[::-1])


def palindrome_checker(x):
    if (str(x) != (str(x))[::-1]):
        return False
    palindrome_string = binary_finder(x)
    if (palindrome_string[0] == '0' or palindrome_string != palindrome_string[::-1]):
        return False
    return True

for i in range (1,1000000):
    if(palindrome_checker(i)):
        answer += i

print(answer)
    
    


