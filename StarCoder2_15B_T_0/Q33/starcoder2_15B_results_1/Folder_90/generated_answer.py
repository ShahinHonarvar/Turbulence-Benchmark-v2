def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 142 and i < 145 and (c > '4') and (c <= 'o'):
            vowels.append(c)
    return vowels