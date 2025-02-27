def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 13 and i < 35 and (c in 'AEIOU') and (ord(c) > ord('8')) and (ord(c) <= ord('F')):
            vowels.append(c)
    return vowels