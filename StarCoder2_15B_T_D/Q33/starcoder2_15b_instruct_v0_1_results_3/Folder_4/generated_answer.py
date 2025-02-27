def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 40 <= i < 91 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'A') and (c <= 'x'):
            vowels.append(c)
    return vowels