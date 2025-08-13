def top_right_diagonal(x):
    running_total = 0
    for i in range(0,x):
        running_total += ((2 * (i+1)) + 1) ** 2
    return running_total

def other_diags(x, offset):
    running_total = 0      # keep: includes the center (1) for this diagonal
    current = 1            # NEW: track the current corner value
    for i in range(0, x):  # keep: i = 0..x-1 gives steps: offset, offset+8, ...
        current += ((8 * i) + offset)   # change: advance to the next corner
        running_total += current        # change: accumulate the corner value
    return running_total



def grid_solver(x):
    grid_size_reduced = int((x-1)/2)
    return top_right_diagonal(grid_size_reduced) + other_diags(grid_size_reduced, 2) + other_diags(grid_size_reduced, 4) + other_diags(grid_size_reduced, 6) + 1



print(grid_solver(1001))



