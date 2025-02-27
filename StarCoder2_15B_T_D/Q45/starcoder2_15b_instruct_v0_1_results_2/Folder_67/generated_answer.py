import re

def palindromes_between_indices(s):
    pattern = re.compile('[a-z]{2,6}', re.I)
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if len(match) >= 5 and match == match[::-1]:
            palindromes.add(match)
    return palindromes