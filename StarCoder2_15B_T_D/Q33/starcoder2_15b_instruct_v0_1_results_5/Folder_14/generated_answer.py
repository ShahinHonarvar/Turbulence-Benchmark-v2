import re

def return_vowels(string):
    pattern = '[a-z]'
    matches = re.findall(pattern, string)
    vowels = 'aeiou'
    result = []
    for match in matches:
        if match in vowels and match > '9' and (match <= 'O'):
            result.append(match)
    return result