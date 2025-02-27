import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(26) + ',' + str(33) + '}'
    sub_string = string[65:100]
    palindromes = set(re.findall(pattern, sub_string, flags=re.IGNORECASE))
    return palindromes