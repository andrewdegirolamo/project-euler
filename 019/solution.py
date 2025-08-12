current_year = 1901
day_of_week = 2
sundays = 0

def year_day_finder():
    global current_year, day_of_week, sundays
    for i in range(1, 13):
        if(day_of_week % 7 == 0):
            sundays += 1
        if (i == 2):
            if (current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0)):
                day_of_week += 29
            else:
                day_of_week += 28
        elif (i == 4 or i == 6 or i == 9 or i == 11):
            day_of_week += 30
        else:
            day_of_week += 31
    current_year += 1

while current_year < 2001:
    year_day_finder()

print(sundays)
            
            

