def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 11 and i < 53 and c.isalpha() and (c.lower() in 'aeiou') and (c > '+') and (c <= 'W'):
            vowels.append(c)
    return vowels