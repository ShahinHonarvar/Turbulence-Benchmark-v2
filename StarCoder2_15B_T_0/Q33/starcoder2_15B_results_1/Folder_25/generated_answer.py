def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 28 and i < 76 and c.isalpha() and (c.lower() in 'aeiou') and (c > '+') and (c <= 'z'):
            vowels.append(c)
    return vowels