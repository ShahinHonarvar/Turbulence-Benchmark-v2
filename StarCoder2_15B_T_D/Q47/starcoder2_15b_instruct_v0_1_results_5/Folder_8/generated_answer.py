import re

def palindromes_of_specific_lengths(string):
    substring = string[17:73]
    pattern = '[A-Za-z]{' + str(50) + ',' + str(51) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes