def return_vowels(string):
    vowels = []
    for c in string[64:82]:
        if c.isalpha() and c.lower() > 'p' and (c.lower() <= 'z'):
            vowels.append(c)
    return vowels