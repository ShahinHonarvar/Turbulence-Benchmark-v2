def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i > 0 and i < 5 and c.isalpha() and (c.lower() in 'aeiou') and (c > '!') and (c <= 'j'):
            vowels.append(c)
    return vowels