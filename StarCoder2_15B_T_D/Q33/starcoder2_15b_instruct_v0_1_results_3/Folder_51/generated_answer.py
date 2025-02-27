import re

def return_vowels(string):
    pattern = '[AEIOU]{57,68}'
    matches = re.findall(pattern, string)
    return [match for match in matches if match > 'M' and match <= 'X']