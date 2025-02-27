import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(23) + ',' + str(36) + '}'
    palindromes = set(re.findall(pattern, string[18:66]))
    return palindromes