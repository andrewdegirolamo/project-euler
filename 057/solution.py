num, denom, counter, answer = 3, 2, 1, 0
while counter != 1001:
    num, denom = num + 2*denom, num + denom
    if (len(str(num)) > len(str(denom))):
        answer += 1
    counter +=1
print(answer)
