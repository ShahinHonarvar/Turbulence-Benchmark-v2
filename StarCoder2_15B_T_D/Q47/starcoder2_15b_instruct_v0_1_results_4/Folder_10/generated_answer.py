import re

def palindromes_of_specific_lengths(string):
    substring = string[16:61]
    pattern = re.compile('[a-zA-Z]{16,39}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindromes.add(match.group().lower())
    return palindromes