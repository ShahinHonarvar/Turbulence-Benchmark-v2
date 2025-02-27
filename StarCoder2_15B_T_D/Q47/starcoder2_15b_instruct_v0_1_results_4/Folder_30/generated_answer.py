import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(55) + ',' + str(71) + '}'
    palindromes = set(re.findall(pattern, string[14:91]))
    return palindromes