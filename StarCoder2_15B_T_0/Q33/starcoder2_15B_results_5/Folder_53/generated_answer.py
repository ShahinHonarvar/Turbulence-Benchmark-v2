def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 27 and i < 57 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'o') and (c <= 'w'):
            vowels.append(c)
    return vowels