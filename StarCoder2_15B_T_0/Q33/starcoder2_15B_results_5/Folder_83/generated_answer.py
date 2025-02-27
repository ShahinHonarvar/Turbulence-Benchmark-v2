def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 90 <= i < 97 and c.isalpha() and (c.lower() in 'aeiou') and (c > '_') and (c <= 'x'):
            vowels.append(c)
    return vowels