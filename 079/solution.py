numbers = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

def digitize(x):
    return [int(digit) for digit in str(x)]

cant_be_first =[]
for i in range(1,50):
    active_digits = digitize(numbers[i - 1])
    cant_be_first.append(active_digits[1])
    cant_be_first.append(active_digits[2])


for i in range(0,10):
    if i not in cant_be_first and i != 4 and i != 5:
        print(i)

# 7 IS THE FIRST NUMBER

cant_be_last =[]
for i in range(1,50):
    active_digits = digitize(numbers[i - 1])
    cant_be_last.append(active_digits[0])
    cant_be_last.append(active_digits[1])


for i in range(0,10):
    if i not in cant_be_last and i != 4 and i != 5:
        print(i)

# 0 IS THE LAST NUMBER
new_numbers = []
for i in range(len(numbers)):
    if (7 not in digitize(numbers[i]) and 0 not in digitize(numbers[i])):
        new_numbers.append(numbers[i])

print(new_numbers)

numbers = new_numbers

cant_be_first =[]
for i in range(1,len(numbers) + 1):
    active_digits = digitize(numbers[i - 1])
    cant_be_first.append(active_digits[1])
    cant_be_first.append(active_digits[2])


for i in range(0,10):
    if i not in cant_be_first and i != 4 and i != 5 and i != 7 and i != 0:
        print(i)

# 7 IS THE FIRST NUMBER

cant_be_last =[]
for i in range(1,len(numbers) + 1):
    active_digits = digitize(numbers[i - 1])
    cant_be_last.append(active_digits[0])
    cant_be_last.append(active_digits[1])


for i in range(0,10):
    if i not in cant_be_last and i != 4 and i != 5 and i != 7 and i != 0:
        print(i)

# now we know 7 3 _ _ _ _ 9 0

new_numbers = []
for i in range(len(numbers)):
    if (3 not in digitize(numbers[i]) and 9 not in digitize(numbers[i])):
        new_numbers.append(numbers[i])

print(new_numbers)

# now we know that it's 7 3 1 6 _ _ 9 8

# now the existence of 728 in the number list proves the answer to be 7 3 1 6 2 8 9 0

# definitely could have made a more elegant solution, will revisit