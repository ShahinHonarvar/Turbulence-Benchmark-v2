def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if c in 'AEIOU' and 56 <= i < 96 and ('&' < c <= 'T'):
            vowels.append(c)
    return vowels