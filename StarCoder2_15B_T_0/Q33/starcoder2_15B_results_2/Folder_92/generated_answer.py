def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if i >= 3 and i < 8 and c.isalpha() and (c.lower() in 'aeiou') and (c > ';') and (c <= 'D'):
            vowels.append(c)
    return vowels