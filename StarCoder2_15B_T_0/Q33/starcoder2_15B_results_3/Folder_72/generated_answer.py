def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 37 and i < 57 and c.isalpha() and (c.lower() in 'aeiou') and (c > '*') and (c <= 'P'):
            vowels.append(c)
    return vowels