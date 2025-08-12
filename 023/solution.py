answer = 0

def divisor_finder(x):
    divisor_list = []
    for i in range(1,x):
        if(x % i == 0):
            divisor_list.append(i)
    return divisor_list

def abundance_checker(x):
    divisors = divisor_finder(x)
    if (sum(divisors) > x):
        return True
    else:
        return False
    
abundants = []
for i in range(1, 28124):
    if abundance_checker(i):
        abundants.append(i)
    

abundant_sums = [False]*28124

def sum_checker(x):
    for i in range(x):
        other_value = x - i
        if (abundance_checker(other_value) and abundance_checker(i)):
            return True
    return False
        
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s < len(abundant_sums):
            abundant_sums[s] = True
        else:
            break

for i in range(28123):
    if not abundant_sums[i]:
        answer += i

print(answer)
