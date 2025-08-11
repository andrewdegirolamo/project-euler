answer = 0
sequence = [0,1]
new_fib = 1

while new_fib < 4000000:
    fib_helper = len(sequence)
    new_fib = sequence[fib_helper - 1] + sequence[fib_helper - 2]
    sequence.append(new_fib)
    if new_fib % 2 == 0:
        answer += new_fib
print(answer)