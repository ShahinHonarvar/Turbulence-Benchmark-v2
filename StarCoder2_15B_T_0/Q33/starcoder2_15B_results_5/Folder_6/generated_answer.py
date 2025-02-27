def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 20 and i < 34 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'U') and (c <= 'i'):
            vowels.append(c)
    return vowels