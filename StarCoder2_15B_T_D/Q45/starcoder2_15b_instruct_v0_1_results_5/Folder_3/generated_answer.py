import re

def palindromes_between_indices(string):
    pattern = '[a-z]{' + str(7) + ',' + str(9) + '}'
    matches = re.findall(pattern, string.lower())
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes