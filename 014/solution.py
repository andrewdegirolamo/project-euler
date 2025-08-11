answer = 0
current_high = 0

def iterative_sequence(x):
    terms = 1
    starter = x
    while starter != 1:
        if starter % 2 == 0:
            starter = starter/2
        else:
            starter = (starter * 3) + 1
        terms +=1
    return terms



for i in range(1,1000001):
    if (iterative_sequence(i) > current_high):
        answer = i
        current_high = iterative_sequence(answer)

print(answer)
