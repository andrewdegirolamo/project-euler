def distinct_solver(a,b):
    distinct_terms = []
    for x in range(a,b+1):
        for y in range(a,b+1):
            result = x ** y
            if result not in distinct_terms:
                distinct_terms.append(result)
    print(sorted(distinct_terms))
    print(len(distinct_terms))

distinct_solver(2,100)
