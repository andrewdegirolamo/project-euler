import math

def find_pentagonals(x):
    pentagonals = []
    for i in range(1,x+1):
        pentagonals.append((i*(3*i - 1)) // 2)
    return pentagonals

def pentagonal_checker(x):
    if x < 0:
        return False
    n = ((math.sqrt((24 * x + 1))) + 1) / 6
    if ( n > 0 and n.is_integer()):
        return True
    else:
        return False


pentagons = find_pentagonals(10000)
possibles = []
for a in range(len(pentagons)):
    for b in range(len(pentagons)):
        if (pentagonal_checker(pentagons[a] + pentagons[b]) and pentagonal_checker(pentagons[a] - pentagons[b])):
            possibles.append(abs(pentagons[b]-pentagons[a]))

print(possibles)

