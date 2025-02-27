def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 8 and i < 9 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'Y') and (c <= 's'):
            vowels.append(c)
    return vowels