def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 604 and i < 949 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'N') and (c <= 'U'):
            vowels.append(c)
    return vowels