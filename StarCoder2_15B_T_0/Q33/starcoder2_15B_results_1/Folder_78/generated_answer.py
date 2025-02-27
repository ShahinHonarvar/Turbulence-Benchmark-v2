def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 46 and i < 90 and c.isalpha() and (c.lower() in 'aeiou') and (c > '@') and (c <= '['):
            vowels.append(c)
    return vowels