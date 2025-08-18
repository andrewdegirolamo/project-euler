def rectangle_finder(x,y):
    return 0.25 * (x*y) * ((x+1)*(y+1))

current_closest_tracker = 500000
best_x, best_y = 0,0
for x in range(1,100):
    for y in range(1,100):
        if(abs(((rectangle_finder(x,y)))-2000000) < current_closest_tracker):
            current_closest_tracker = abs(((rectangle_finder(x,y)))-2000000)
            best_x, best_y = x,y

print(best_x * best_y)



        
