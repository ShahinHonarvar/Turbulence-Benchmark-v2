def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 149 and i < 313 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'M') and (c <= 'j'):
            vowels.append(c)
    return vowels