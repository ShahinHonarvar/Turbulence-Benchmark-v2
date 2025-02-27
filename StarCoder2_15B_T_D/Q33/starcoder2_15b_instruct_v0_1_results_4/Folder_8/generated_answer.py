def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 64 < i < 82 and c.isalpha() and (c.lower() > 'p') and (c.lower() <= 'z'):
            vowels.append(c)
    return vowels