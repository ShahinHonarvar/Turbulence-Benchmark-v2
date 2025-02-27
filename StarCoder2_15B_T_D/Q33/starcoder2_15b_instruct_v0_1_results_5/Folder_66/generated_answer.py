def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 63 <= i < 79 and c.isalpha() and (c.lower() in 'aeiou') and (c.lower() > 'd') and (c.lower() <= 'y'):
            vowels.append(c)
    return vowels