import re

def palindromes_of_specific_lengths(string):
    substring = string[62:89]
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(21) + '}'
    matched_palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return matched_palindromes