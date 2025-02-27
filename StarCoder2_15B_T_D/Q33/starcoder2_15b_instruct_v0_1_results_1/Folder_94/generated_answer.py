def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 40 and i < 94 and (c in 'AEIOU') and (c > '4') and (c <= 'H'):
            vowels.append(c)
    return vowels