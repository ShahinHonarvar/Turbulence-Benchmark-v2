import re

def palindromes_of_specific_lengths(string):
    substring = string[27:78]
    regex = re.compile('[a-zA-Z]{18,19}')
    matches = regex.findall(substring)
    return set(matches)