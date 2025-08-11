import math

#x = one side of square grid

def lattice_paths(x): 
    n = x + x
    r = x
    return(math.factorial(n)/((math.factorial(r))*(math.factorial(n-r))))

print(lattice_paths(20))