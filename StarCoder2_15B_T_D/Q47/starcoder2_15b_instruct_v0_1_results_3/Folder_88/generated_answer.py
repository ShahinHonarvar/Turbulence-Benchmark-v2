import re

def palindromes_of_specific_lengths(string):
    if len(string) < 88:
        return set()
    substring = string[11:88]
    pattern = re.compile('[a-zA-Z]{4,5}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes