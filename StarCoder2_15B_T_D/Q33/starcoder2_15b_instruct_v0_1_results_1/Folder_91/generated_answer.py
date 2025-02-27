import re

def return_vowels(s):
    vowels = []
    for i, c in enumerate(s):
        if i >= 4 and i < 8 and c.isalpha() and (c.lower() in 'aeiou') and (c > 'P') and (c <= 'r'):
            vowels.append(c)
    return vowels