def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 328 and i < 455 and c.isalpha() and (c.lower() in 'aeiou'):
            vowels.append(c)
    return vowels