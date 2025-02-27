import re

def return_vowels(string):
    pattern = '[a-z]'
    matches = re.findall(pattern, string[51:77])
    return [match for match in matches if match > '4' and match <= '=']