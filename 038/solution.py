max_pali_found = 0

def sequence_finder(x,depth):
    returning = []
    for i in range(1,depth+1):
        returning.append(x*i)
    stringy = "".join(str(digit) for digit in returning)
    sorted_stringy = "".join(sorted(stringy))
    if (sorted_stringy == '123456789'):
        return int(stringy)
    else:
        return False


for i in range(1000,10000): # did a little manual brute-forcing here
    dep = 2
    if(sequence_finder(i,dep) != False):
        if (sequence_finder(i,dep) > max_pali_found):
            max_pali_found = sequence_finder(i,dep)
print(max_pali_found)
    


