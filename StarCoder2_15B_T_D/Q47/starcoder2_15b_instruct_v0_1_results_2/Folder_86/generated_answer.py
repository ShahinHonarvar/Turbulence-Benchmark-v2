import re

def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    pattern = '[a-zA-Z]{' + str(34) + ',' + str(55) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes