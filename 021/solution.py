answer = 0

def divisor_finder(x):
    divisor_list = []
    for i in range(1,x):
        if(x % i == 0):
            divisor_list.append(i)
    return divisor_list


def amicable_checker(x):
    first_run = sum(divisor_finder(x))
    second_run = sum(divisor_finder(first_run))
    if(second_run == x and first_run != second_run):
        return True
    else:
        return False
    

for i in range (1,10000):
    if(amicable_checker(i) == True):
        answer += i

print(answer)