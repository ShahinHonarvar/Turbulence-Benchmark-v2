def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 20 and i < 41 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'K') and (c <= 'Z'):
            vowels.append(c)
    return vowels