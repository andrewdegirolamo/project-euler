def reversed_number(x):
    reversed_str = str(x)[::-1]
    reversed_num = int(reversed_str)
    return reversed_num

def is_lychrel(x):
    steps = 0
    i = x + reversed_number(x)
    while (i != reversed_number(i)):
        i = i + reversed_number(i)
        steps +=  1
        if(steps > 50):
            return True
    return False
        
    

counter = 0
for i in range(1,10000):
    if(is_lychrel(i)):
        counter +=1

print(counter)