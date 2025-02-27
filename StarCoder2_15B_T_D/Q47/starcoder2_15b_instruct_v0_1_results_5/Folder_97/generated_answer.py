import re

def palindromes_of_specific_lengths(string):
    sub_string = string[28:95]
    pattern = '[a-zA-Z]{' + str(38) + ',' + str(49) + '}'
    palindromes = set(re.findall(pattern, sub_string, flags=re.IGNORECASE))
    return palindromes