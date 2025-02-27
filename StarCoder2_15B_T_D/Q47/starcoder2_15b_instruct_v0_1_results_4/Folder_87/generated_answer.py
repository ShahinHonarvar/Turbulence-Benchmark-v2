import re

def palindromes_of_specific_lengths(string):
    sub_string = string[11:94]
    pattern = '[a-zA-Z]{' + str(34) + ',' + str(54) + '}'
    palindromes = set(re.findall(pattern, sub_string, flags=re.IGNORECASE))
    return palindromes