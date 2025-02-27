def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 20 and i < 41 and c.isalpha() and (c.upper() > 'K') and (c.upper() <= 'Z'):
            vowels.append(c)
    return vowels