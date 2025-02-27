import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-z]+', re.IGNORECASE)
    matches = pattern.findall(string)
    palindromes = set()
    for match in matches:
        if len(match) >= 3 and match[1:4] == match[1:4][::-1]:
            palindromes.add(match)
    return palindromes