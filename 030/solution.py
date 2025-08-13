matches = []

def check_sums(x,power):
    stringify = [int(d) for d in str(x)]
    running_total = 0
    for i in range(len(stringify)):
        running_total += stringify[i] ** power
    if running_total == x:
        return True
    else:
        return False
    


for i in range(2,10000000):
    if check_sums(i,5):
        matches.append(i)

print(sum(matches))

