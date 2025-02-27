import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[A-Za-z]{13,49}')
    palindromes = set()
    for match in pattern.finditer(string[17:96]):
        palindromes.add(match.group().lower())
    return palindromes