def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 63 and i < 79 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'D') and (c <= 'y'):
            vowels.append(c)
    return vowels