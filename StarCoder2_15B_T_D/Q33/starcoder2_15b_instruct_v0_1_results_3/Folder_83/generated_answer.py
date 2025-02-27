import re

def return_vowels(string):
    pattern = '[aeiou]{90,97}'
    matches = re.findall(pattern, string)
    return matches