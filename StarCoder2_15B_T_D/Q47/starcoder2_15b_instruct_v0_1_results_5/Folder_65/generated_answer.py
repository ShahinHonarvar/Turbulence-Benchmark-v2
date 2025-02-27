import re

def palindromes_of_specific_lengths(string):
    substring = string[15:96]
    pattern = '[a-zA-Z]{' + str(20) + ',' + str(66) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes