def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i in range(29, 31) and c.isalpha() and (c > 'a') and (c <= 'f'):
            vowels.append(c)
    return vowels