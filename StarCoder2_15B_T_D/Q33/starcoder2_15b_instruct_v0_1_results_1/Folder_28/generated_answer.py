def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 41 and i < 50 and c.isupper() and (c in 'AEIOU') and ('W' < c <= '['):
            vowels.append(c)
    return vowels