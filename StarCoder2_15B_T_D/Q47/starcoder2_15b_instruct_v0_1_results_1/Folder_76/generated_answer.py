import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(154) + ',' + str(182) + '}'
    substring = string[101:293]
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes