def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 60 and i < 99 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'j') and (c <= 'n'):
            vowels.append(c)
    return vowels