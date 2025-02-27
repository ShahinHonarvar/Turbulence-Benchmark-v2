import re

def return_vowels(string):
    vowels = []
    pattern = '[a-j][!-j]'
    matches = re.findall(pattern, string[1:5])
    for match in matches:
        vowels.append(match[0])
    return vowels