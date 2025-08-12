from itertools import permutations

s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

a = (list(s))
permutation_list = []

for p in permutations(a):
    permutation_list.append(p)

print(permutation_list[999999])
