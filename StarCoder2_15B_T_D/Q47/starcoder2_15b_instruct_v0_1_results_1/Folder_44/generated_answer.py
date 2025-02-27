import re

def palindromes_of_specific_lengths(string):
    sub_string = string[18:99]
    pattern = '[a-zA-Z]{' + str(31) + ',' + str(51) + '}'
    palindromes = set(re.findall(pattern, sub_string, flags=re.IGNORECASE))
    return palindromes