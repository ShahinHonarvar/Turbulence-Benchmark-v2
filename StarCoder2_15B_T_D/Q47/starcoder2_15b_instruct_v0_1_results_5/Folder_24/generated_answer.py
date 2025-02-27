import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[12:93]
    pattern = '[a-zA-Z]{' + str(42) + ',' + str(77) + '}'
    for match in re.finditer(pattern, substring, re.I):
        palindromes.add(match.group().lower())
    return palindromes