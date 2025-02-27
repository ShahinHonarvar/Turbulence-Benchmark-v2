import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{18,36}')
    matches = pattern.findall(string[10:60])
    return {match.lower() for match in matches if match == match[::-1]}