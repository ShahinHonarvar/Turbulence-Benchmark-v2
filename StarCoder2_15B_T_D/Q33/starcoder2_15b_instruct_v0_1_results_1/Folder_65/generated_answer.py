def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 71 and i < 88 and (c > '9') and (c <= 'P'):
            vowels.append(c)
    return vowels