fib_sequence = [1, 1]

def find_next_fib():
    current_max = len(fib_sequence)
    fib_sequence.append(fib_sequence[current_max - 1] + fib_sequence[current_max - 2])

while len(str(fib_sequence[-1])) < 1000:
    find_next_fib()
    print(fib_sequence[-1])

print(len(fib_sequence))
