import re

def return_vowels(string):
    pattern = re.compile('[a-zA-Z]')
    vowels = []
    for i, c in enumerate(string):
        if i >= 149 and i < 313 and (c.upper() in 'AEIOU') and (c.upper() > 'M') and (c.upper() <= 'J'):
            vowels.append(c)
    return vowels