import re

def return_vowels(string):
    pattern = '[AEIOU]{528,606}'
    matches = re.findall(pattern, string)
    vowels = []
    for match in matches:
        for char in match:
            if char > 'M' and char <= 'X':
                vowels.append(char)
    return vowels