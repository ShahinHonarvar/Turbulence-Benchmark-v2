def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 260 and i < 322 and c.isalpha() and (c.lower() in 'aeiou') and (c > '%') and (c <= 'U'):
            vowels.append(c)
    return vowels