import re

def palindromes_of_specific_lengths(string):
    sub_string = string[63:71]
    pattern = '[a-zA-Z]{' + str(4) + ',' + str(5) + '}'
    palindromes = set(re.findall(pattern, sub_string, flags=re.IGNORECASE))
    return palindromes