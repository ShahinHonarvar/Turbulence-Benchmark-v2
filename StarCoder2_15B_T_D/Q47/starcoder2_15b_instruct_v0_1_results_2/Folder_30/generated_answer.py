import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(55) + ',' + str(71) + '}'
    substring = string[14:91]
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes