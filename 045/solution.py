triangle = []
pentagon = []
hexagonal = []

def finders(x):
    for i in range(1, x+1):
        triangle.append((i*(i+1))//2)
        pentagon.append((i*(3*i-1))//2)
        hexagonal.append((i*(2*i-1)))

finders(100000)

answer = 0
counter = 285

while answer == 0:
    print(counter)
    if(triangle[counter] in pentagon and triangle[counter] in hexagonal):
        print(triangle[counter])
        answer = 1
    counter += 1

