current_number = 1

big_kahuna = ""

while len(big_kahuna) < 1000005:
    big_kahuna += str(current_number)
    current_number +=1

sorted_big_kahuna = list(big_kahuna)

answer = int(sorted_big_kahuna[0]) * int(sorted_big_kahuna[9]) * int(sorted_big_kahuna[99]) * int(sorted_big_kahuna[999]) * int(sorted_big_kahuna[9999]) * int(sorted_big_kahuna[99999]) * int(sorted_big_kahuna[999999])

print(answer)