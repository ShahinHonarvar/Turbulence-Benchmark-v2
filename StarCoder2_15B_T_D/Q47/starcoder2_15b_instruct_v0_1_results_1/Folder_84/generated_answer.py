import re

def palindromes_of_specific_lengths(string):
    substring = string[23:78]
    pattern = '[a-zA-Z]{' + str(13) + ',' + str(40) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes