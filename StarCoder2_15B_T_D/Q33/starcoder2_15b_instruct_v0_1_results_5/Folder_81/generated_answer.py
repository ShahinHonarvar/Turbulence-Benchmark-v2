def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 20 and i < 43 and (c > '5') and (c <= 'M'):
            vowels.append(c)
    return vowels