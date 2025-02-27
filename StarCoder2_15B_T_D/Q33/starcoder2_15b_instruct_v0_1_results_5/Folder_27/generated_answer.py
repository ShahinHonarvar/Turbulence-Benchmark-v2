def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 29 and i < 31 and c.isalpha() and ('a' < c <= 'f'):
            vowels.append(c)
    return vowels