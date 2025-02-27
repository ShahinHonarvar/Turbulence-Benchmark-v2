import re

def return_vowels(string):
    pattern = '[a-zA-Z]'
    matches = re.findall(pattern, string)
    vowels = [c for c in matches if c.isalpha() and c.lower() in 'aeiou' and ('i' < c <= 'x')]
    return vowels[74:96]