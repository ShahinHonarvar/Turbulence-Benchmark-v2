import re

def palindromes_between_indices(string):
    pattern = '[a-z]{3,7}'
    matches = re.findall(pattern, string.lower())
    palindromes = set()
    for match in matches:
        if len(match) >= 6 and match == match[::-1]:
            palindromes.add(match)
    return palindromes