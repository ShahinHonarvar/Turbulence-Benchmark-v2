def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 47 and i < 61 and c.isalpha() and (c.lower() in 'aeiou') and (c > '9') and (c <= 'O'):
            vowels.append(c)
    return vowels