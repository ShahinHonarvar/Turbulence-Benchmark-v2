def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 21 and i < 23 and c.isalpha() and (c.lower() in 'aeiou') and (c <= 'n'):
            vowels.append(c)
    return vowels