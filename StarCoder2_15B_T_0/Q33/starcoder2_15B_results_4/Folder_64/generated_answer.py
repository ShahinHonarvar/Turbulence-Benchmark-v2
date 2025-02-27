def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 1 and i < 7 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'F') and (c <= 'j'):
            vowels.append(c)
    return vowels