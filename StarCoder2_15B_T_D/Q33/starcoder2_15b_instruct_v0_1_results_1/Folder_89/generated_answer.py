def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 50 and i < 51 and c.isalpha() and (c in 'aeiou') and (c <= 'v'):
            vowels.append(c)
    return vowels