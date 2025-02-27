import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[26:85]
    pattern = re.compile('[a-zA-Z]{30,46}')
    for match in pattern.finditer(substring):
        palindromes.add(match.group().lower())
    return palindromes