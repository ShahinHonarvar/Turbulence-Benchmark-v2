import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(49) + ',' + str(51) + '}'
    substring = string[27:96]
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes