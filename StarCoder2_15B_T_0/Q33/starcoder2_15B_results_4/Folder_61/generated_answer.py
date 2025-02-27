def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i > 0 and i < 4 and (c.lower() in 'aeiou') and ('c' < c.lower() <= 'i'):
            vowels.append(c)
    return vowels