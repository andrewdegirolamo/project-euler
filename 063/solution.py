import math
values = set()
for a in range(1,10):
    for x in range(1,22):
        values.add(a**x)

def checker(x):
    digit_count = len(str(x))
    root = (x ** (1 / digit_count))
    return math.isclose(root, round(root))

counter = 0
for v in values:
    if (checker(v)):
        counter +=1

print(counter)