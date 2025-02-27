def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 56 <= i < 96 and c.isalpha() and (c.lower() in 'aeiou') and (c > '&') and (c <= 'T'):
            vowels.append(c)
    return vowels