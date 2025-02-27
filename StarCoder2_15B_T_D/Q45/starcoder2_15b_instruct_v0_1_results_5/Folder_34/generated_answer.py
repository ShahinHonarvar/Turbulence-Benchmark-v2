import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-z]{4,}')
    matches = pattern.findall(string.lower())
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes