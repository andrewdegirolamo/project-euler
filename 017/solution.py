
def natural_language_word(number):
    pre_twenty = {
        1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
        15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'
    }
    if number < 20:
        return pre_twenty[number]

    pre_hundreds = {
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'
    }
    if number < 100:
        tens = pre_hundreds[(number // 10) * 10]
        return tens if number % 10 == 0 else tens + pre_twenty[number % 10]

    if number < 1000:
        hundreds = pre_twenty[number // 100] + 'hundred'
        return hundreds if number % 100 == 0 else hundreds + 'and' + natural_language_word(number % 100)

    if number < 1000000:
        thousands = natural_language_word(number // 1000) + 'thousand'
        return thousands if number % 1000 == 0 else thousands + 'and' + natural_language_word(number % 1000)

def character_counter(x):
    tracker_string = ""
    for i in range(1,x+1):
        tracker_string = tracker_string + natural_language_word(i)
    return (len(tracker_string))

print(character_counter(1000))
        


