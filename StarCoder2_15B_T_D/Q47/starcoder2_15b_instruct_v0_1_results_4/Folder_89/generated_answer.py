import re

def palindromes_of_specific_lengths(string):
    substring = string[18:89]
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(14) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes