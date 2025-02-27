def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 86 and i < 99 and c.isalpha() and (c.lower() > 'e') and (c.lower() <= 'r'):
            vowels.append(c)
    return vowels