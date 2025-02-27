def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 56 and i < 68 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'M') and (c <= 'X'):
            vowels.append(c)
    return vowels