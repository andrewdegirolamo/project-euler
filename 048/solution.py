def self_power_finder(x):
    results = []
    for i in range(1, x+1):
        results.append(i**i)
    return(sum(results))

answer_string = str(self_power_finder(1000))

print(answer_string[-10:])

