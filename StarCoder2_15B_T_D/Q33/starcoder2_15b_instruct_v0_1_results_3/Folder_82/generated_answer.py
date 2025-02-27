import re

def return_vowels(string):
    vowels = []
    pattern = '[E-r]'
    matches = re.findall(pattern, string[86:99])
    for match in matches:
        if match in 'aeiou':
            vowels.append(match)
    return vowels