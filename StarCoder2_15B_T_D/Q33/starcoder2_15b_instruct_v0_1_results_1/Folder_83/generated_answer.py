def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 90 and i < 97 and (c > '_') and (c <= 'x'):
            vowels.append(c)
    return vowels