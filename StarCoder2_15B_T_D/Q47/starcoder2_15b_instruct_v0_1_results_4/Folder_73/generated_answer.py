import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(22) + ',' + str(33) + '}'
    substring = string[21:63]
    palindromes = set(re.findall(pattern, substring, re.IGNORECASE))
    return palindromes