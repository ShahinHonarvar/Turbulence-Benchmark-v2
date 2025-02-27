def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 32 and i < 97 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'Q') and (c <= ']'):
            vowels.append(c)
    return vowels