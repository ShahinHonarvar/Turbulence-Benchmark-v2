def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 23 and i < 85 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'W') and (c <= 'v'):
            vowels.append(c)
    return vowels