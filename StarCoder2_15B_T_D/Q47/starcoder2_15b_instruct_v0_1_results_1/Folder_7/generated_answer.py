import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[119:257]
    pattern = re.compile('[a-zA-Z]{104,123}')
    for match in pattern.finditer(substring):
        palindromes.add(match.group().lower())
    return palindromes