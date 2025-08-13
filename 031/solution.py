answer = 0
for a in range(0, 2):
    for b in range(0, 3):
        for c in range(0, 5):
            for d in range(0, 11):
                for e in range(0, 21):
                    for f in range(0, 41):
                        for g in range(0, 101):
                            for h in range(0, 201):
                                total = (
                                    a*200 + b*100 + c*50 + d*20 +
                                    e*10 + f*5 + g*2 + h
                                )
                                if total == 200:
                                    answer += 1
print(answer)
