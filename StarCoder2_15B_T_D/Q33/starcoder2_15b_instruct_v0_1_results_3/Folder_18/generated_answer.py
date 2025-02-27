def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 528 and i < 606 and c.isalpha() and (c.lower() > 'm') and (c.lower() <= 'x'):
            vowels.append(c)
    return vowels