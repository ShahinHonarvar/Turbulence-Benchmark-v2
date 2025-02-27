import re

def palindromes_between_indices(string):
    pattern = '[a-z]{3,8}'
    matches = re.findall(pattern, string.lower())
    palindromes = set()
    for match in matches:
        if len(match) >= 7 and match == match[::-1]:
            palindromes.add(match)
    return palindromes