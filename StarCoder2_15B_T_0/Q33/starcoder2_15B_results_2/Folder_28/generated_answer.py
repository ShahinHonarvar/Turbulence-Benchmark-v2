def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 41 and i < 50 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'W') and (c <= '['):
            vowels.append(c)
    return vowels