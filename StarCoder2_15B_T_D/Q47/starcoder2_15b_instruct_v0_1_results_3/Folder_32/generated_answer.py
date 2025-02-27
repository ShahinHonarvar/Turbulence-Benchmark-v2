import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{43,47}')
    substring = string[16:78]
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes