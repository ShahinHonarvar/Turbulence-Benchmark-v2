import re

def palindromes_of_specific_lengths(string):
    substring = string[29:97]
    pattern = re.compile('[a-zA-Z]{12,18}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindromes.add(match.group().lower())
    return palindromes