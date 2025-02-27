def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 74 and i < 96 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'I') and (c <= 'X'):
            vowels.append(c)
    return vowels