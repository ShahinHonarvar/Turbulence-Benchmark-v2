import re

def return_vowels(string):
    pattern = '[a-z]'
    matches = re.findall(pattern, string[20:34])
    vowels = [match for match in matches if match > 'u' and match <= 'i']
    return vowels