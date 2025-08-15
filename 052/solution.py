def sorted_digits(x):
    number_str = str(x)
    sorted_digits = sorted(number_str)
    sorted_str = "".join(sorted_digits)
    return sorted_str


def poc(x):
    if(sorted_digits(x) == sorted_digits(2*x)):
        if(sorted_digits(x) == sorted_digits(3*x)):
            if(sorted_digits(x) == sorted_digits(4*x)):
                if(sorted_digits(x) == sorted_digits(5*x)):
                    if(sorted_digits(x) == sorted_digits(6*x)):
                        return x
    return False

for i in range(1,1000000):
    if (poc(i) != False):
        print(i)
        break
