finished_answer = 1

def divisible_checker(range_max,x):
    for i in range(1, range_max+1):
        if(x % i != 0):
            return False
    return True

while divisible_checker(20, finished_answer) == False:
    finished_answer += 1


print(finished_answer)