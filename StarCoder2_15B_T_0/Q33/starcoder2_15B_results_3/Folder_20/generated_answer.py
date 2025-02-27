def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 59 and i < 61 and c.isalpha() and (c.lower() in 'aeiou') and (c > '+') and (c <= 'h'):
            vowels.append(c)
    return vowels