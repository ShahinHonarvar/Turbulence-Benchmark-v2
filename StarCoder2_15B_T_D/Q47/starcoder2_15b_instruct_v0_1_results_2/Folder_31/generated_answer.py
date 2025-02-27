import re

def palindromes_of_specific_lengths(s):
    pattern = re.compile('[a-zA-Z]{37,60}', re.I)
    matches = pattern.findall(s[11:84])
    return set(matches)