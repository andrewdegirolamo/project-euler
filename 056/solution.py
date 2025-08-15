possibles = []
def sum_of_digits(x):
    return sum(map(int, str(x)))

for a in range(1,100):
    for b in range(1,100):
        possibles.append(a ** b)

for i in range(len(possibles)):
    possibles[i] = sum_of_digits(possibles[i])

print(max(possibles))