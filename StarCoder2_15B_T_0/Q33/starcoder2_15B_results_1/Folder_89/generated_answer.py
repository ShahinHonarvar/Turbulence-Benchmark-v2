def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 50 and i < 51 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'c') and (c <= 'v'):
            vowels.append(c)
    return vowels