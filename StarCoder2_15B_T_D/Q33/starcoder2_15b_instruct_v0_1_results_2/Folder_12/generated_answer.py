def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 13 and i < 37 and c.isalpha() and (c.lower() in 'aeiou') and ('Z' < c <= '}'):
            vowels.append(c)
    return vowels