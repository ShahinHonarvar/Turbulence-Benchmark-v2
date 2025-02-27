def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 47 and i < 89 and c.isalpha() and (c.lower() in 'aeiou') and (c > '@') and (c <= 'n'):
            vowels.append(c)
    return vowels