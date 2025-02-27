def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 40 and i < 94 and c.isalpha() and (c.lower() in 'aeiou') and (c > '4') and (c <= 'H'):
            vowels.append(c)
    return vowels