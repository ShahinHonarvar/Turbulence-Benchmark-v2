import re

def palindromes_of_specific_lengths(string):
    substring = string[119:257]
    pattern = re.compile('[a-zA-Z]{104,123}')
    matches = pattern.findall(substring)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes