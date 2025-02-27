def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 3 and i < 9 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'S') and (c <= 'U'):
            vowels.append(c)
    return vowels