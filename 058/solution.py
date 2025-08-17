def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in [2, 7, 61]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

last_top_right = 1
last_top_left = 1
last_down_left = 1
def get_four_positions(layer):
    global last_down_left, last_top_left, last_top_right
    top_right = (layer - 1) * 8 + 2 + last_top_right
    last_top_right = top_right
    top_left = (layer - 1) * 8 + 4 + last_top_left
    last_top_left = top_left
    down_left = (layer - 1) * 8 + 6 + last_down_left
    last_down_left = down_left
    counter = 0
    if(is_prime(down_left)):
        counter +=1
    if(is_prime(top_right)):
        counter +=1
    if(is_prime(top_left)):
        counter +=1
    return counter

num = 0
denom = 1
position_tracker = 1

while num / denom > 0.10 or denom == 1:
    num += get_four_positions(position_tracker)
    denom += 4
    position_tracker += 1

print((position_tracker)*2-1)
