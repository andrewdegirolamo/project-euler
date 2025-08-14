import math

numerators = []
denominators = []

for n in range (10,100):
    for d in range(n+1, 100):
        stringed_num = str(n)
        stringed_denom = str(d)
        if('0' in stringed_denom or '0' in stringed_num):
            continue
        elif(stringed_num[0] == stringed_denom[1]):
            if(int(stringed_num[1]) / int(stringed_denom[0]) == n / d):
                numerators.append(n)
                denominators.append(d)
        elif(stringed_num[1] == stringed_denom[0]):
            if(int(stringed_num[0]) / int(stringed_denom[1]) == n / d):
                numerators.append(n)
                denominators.append(d)

print(math.prod(denominators) // math.prod(numerators))




