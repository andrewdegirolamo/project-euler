def chain_finder(x):
    digits = list(map(int, str(x)))
    total = 0
    for i in range(len(digits)):
        total += digits[i] ** 2
    return total

def number_checker(x):
    active = x
    chain = [x]
    while (chain.count(1) != 2 and chain.count(89) != 2):
        new_active = chain_finder(active)
        chain.append(new_active)
        active = new_active
    if (chain.count(1) == 2):
        return False
    else:
        return True

counter = 0
for i in range(1,10000000):
    if (number_checker(i)):
        counter += 1

print(counter)