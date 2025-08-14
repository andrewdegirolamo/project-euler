def fraction_finder(d):
    visited = {}
    numerator = 1
    position = 0
    while numerator not in visited:
        visited[numerator] = position
        numerator = (numerator * 10) % d
        position += 1
        if numerator == 0:
            return 0
    return position - visited[numerator]

max_denom = 999
best_denom = 0
best_length = 0

for d in range(2, max_denom + 1):
    length = fraction_finder(d)
    if length > best_length:
        best_length = length
        best_denom = d

print(best_denom)
