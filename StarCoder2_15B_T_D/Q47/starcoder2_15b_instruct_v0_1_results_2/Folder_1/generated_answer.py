import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(40) + ',' + str(72) + '}'
    substring = string[15:90]
    palindromes = set(re.findall(pattern, substring))
    return palindromes