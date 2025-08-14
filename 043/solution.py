import itertools

answer = 0

numbers = [0,1,2,3,4,5,6,7,8,9]
pandies = []
for n in itertools.permutations(numbers):
    if n[0] != 0:
        intify = list(map(str, n))
        joined = int(''.join(intify))
        pandies.append(joined)



def substring_checker(x):
    listed = list(str(x))
    checks_divisors = [2,3,5,7,11,13,17]
    dividends = [int(listed[1]+listed[2]+listed[3]), int(listed[2]+listed[3]+listed[4]), int(listed[3]+listed[4]+listed[5]), int(listed[4]+listed[5]+listed[6]), int(listed[5]+listed[6]+listed[7]), int(listed[6]+listed[7]+listed[8]), int(listed[7]+listed[8]+listed[9])]
    for i in range(7):
        if (dividends[i] % checks_divisors[i] != 0):
            return False
    return True

for i in range(len(pandies)):
    if (substring_checker(pandies[i])):
        answer += pandies[i]

print(answer)




