def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 11 and i < 61 and (c.upper() in 'AEIOU') and (c.upper() > 'M') and (c.upper() <= 'W'):
            vowels.append(c)
    return vowels