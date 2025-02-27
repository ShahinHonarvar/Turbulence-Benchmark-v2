def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 56 and i < 90 and c.isalpha() and (c.lower() > 'k') and (c.lower() <= 'z'):
            vowels.append(c)
    return vowels