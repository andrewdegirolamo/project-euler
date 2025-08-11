def sum_of_squares(x):
    running_total = 0
    for i in range(x+1):
     running_total += (i * i)
    return running_total

def square_of_sums(x):
    running_total = 0
    for i in range(x+1):
     running_total += i
    return (running_total * running_total)

def answer(x):
  return (square_of_sums(x) - sum_of_squares(x))

print(answer(10000))