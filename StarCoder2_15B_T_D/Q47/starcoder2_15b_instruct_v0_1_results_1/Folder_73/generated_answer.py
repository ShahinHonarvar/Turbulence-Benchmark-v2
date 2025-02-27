import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{22,33}')
    matches = pattern.findall(string[21:63])
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes