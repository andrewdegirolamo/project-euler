def triangle_brute_checker(x):
    counter = 0
    for a in range(1, x-2):
        for b in range(a, x-1):
                c = x - a - b
                if (a ** 2 + b ** 2 == c ** 2 and a + b + c == x):
                    counter +=1
    return counter

max_counter = 0
highest_p = 0
for i in range(2,1001,2):
    if (max_counter < triangle_brute_checker(i)):
        max_counter = triangle_brute_checker(i)
        highest_p = i

print(highest_p)