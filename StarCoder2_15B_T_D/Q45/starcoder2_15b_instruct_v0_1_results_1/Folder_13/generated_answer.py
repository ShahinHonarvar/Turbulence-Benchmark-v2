import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-z]{3,9}', re.I)
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if len(match) >= 5 and match == match[::-1]:
            palindromes.add(match)
    return palindromes