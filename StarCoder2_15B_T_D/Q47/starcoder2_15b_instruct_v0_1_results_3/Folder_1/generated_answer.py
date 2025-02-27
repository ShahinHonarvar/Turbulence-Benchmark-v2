import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{40,72}')
    matches = pattern.findall(string[15:90])
    return set(matches)