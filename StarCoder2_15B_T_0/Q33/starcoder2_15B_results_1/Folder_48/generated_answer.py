def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 529 and i < 828 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'U') and (c <= 'l'):
            vowels.append(c)
    return vowels