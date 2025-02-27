def return_vowels(string):
    vowels = []
    for i, c in enumerate(string[149:313]):
        if c.lower() in 'aeiou' and c > 'M' and (c <= 'j'):
            vowels.append(c)
    return vowels