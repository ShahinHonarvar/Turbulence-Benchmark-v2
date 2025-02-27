def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 23 and i < 57 and c.isalpha() and (c > '0') and (c <= 'd'):
            vowels.append(c)
    return vowels