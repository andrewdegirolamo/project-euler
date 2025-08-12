answer = 0

with open("names.txt", "r") as file:
    content = file.read()

names = [name.strip().strip('"') for name in content.split(",")]

names.sort()

answer = 0
abc_values = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def word_worth(word):
    stringify = list(word)
    words_worth = 0
    for i in range(len(stringify)):
        words_worth += abc_values[(stringify[i])]
    return words_worth

for i in range(len(names)):
    answer += word_worth(names[i]) * (i + 1)

print(answer)
    


