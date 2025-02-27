import re

def palindromes_of_specific_lengths(string):
    substring = string[62:89]
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(21) + '}'
    palindromes = set(re.findall(pattern, substring, re.IGNORECASE))
    return palindromes