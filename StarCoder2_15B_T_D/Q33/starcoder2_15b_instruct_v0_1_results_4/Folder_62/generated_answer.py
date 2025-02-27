def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 14 and i < 60 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'D') and (c <= 'v'):
            vowels.append(c)
    return vowels