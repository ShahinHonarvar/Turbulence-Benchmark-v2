import re

def palindromes_of_specific_lengths(string):
    substring = string[20:75]
    pattern = '[a-zA-Z]{' + str(36) + ',' + str(42) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes