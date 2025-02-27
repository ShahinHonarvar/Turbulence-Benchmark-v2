import re

def palindromes_of_specific_lengths(string):
    substring = string[11:94]
    pattern = '[a-zA-Z]{' + str(34) + ',' + str(54) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes