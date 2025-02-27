def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 273 and i < 275 and c.isalpha() and (c.lower() > '+') and (c.lower() <= 'o'):
            vowels.append(c)
    return vowels