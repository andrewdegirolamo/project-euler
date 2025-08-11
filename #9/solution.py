import math

first_check = 5

def pythag_finder(x):
    squared_total = x * x
    for a in range(x):
        for b in range(x):
            if (((a * a) + (b * b)) == squared_total):
                if(sum([a,b,x]) == 1000):
                    return math.prod([a,b,x])
    return False

while pythag_finder(first_check) == False:
    first_check += 1

print(pythag_finder(first_check))