def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 21 and i < 59 and c.isalpha() and (c.lower() > 'f') and (c.lower() <= 'a'):
            vowels.append(c)
    return vowels