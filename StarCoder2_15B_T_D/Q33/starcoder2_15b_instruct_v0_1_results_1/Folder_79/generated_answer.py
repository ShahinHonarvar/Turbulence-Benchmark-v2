import re

def return_vowels(string):
    pattern = '[aeiou]{75,96}'
    matches = re.findall(pattern, string)
    filtered_matches = [match for match in matches if match > 'I' and match <= 'X']
    return filtered_matches