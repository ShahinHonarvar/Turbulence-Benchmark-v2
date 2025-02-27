def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 273 and i < 275 and (c > '+') and (c <= 'o'):
            vowels.append(c)
    return vowels