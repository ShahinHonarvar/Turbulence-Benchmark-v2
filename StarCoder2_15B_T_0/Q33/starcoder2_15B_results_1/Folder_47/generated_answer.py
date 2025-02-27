def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 23 and i < 38 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'N') and (c <= 'k'):
            vowels.append(c)
    return vowels