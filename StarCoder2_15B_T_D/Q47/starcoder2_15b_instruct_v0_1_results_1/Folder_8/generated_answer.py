import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(51) + '}'
    substring = string[17:73]
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes