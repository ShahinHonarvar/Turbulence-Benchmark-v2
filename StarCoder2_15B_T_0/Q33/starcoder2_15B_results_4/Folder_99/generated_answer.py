def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 323 and i < 526 and c.isalpha() and (c.lower() in 'aeiou'):
            vowels.append(c)
    return vowels