import re

def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    pattern = re.compile('[a-z]{50,60}')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes