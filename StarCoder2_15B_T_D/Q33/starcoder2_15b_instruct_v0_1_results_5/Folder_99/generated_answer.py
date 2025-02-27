def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if 323 <= i < 526 and c.isalpha() and (c.lower() in 'aeiou') and ('+' < c <= ':'):
            vowels.append(c)
    return vowels