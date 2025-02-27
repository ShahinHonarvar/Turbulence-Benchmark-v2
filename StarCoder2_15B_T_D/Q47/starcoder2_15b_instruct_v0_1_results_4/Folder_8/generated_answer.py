import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(51) + '}'
    palindromes = set(re.findall(pattern, string[17:73]))
    return palindromes