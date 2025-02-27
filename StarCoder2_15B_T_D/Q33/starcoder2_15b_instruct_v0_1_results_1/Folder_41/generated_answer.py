def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 71 and i < 81 and (c > 'a') and (c <= 'U'):
            vowels.append(c)
    return vowels