import re

def palindromes_of_specific_lengths(string):
    substring = string[:301]
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(60) + '}'
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes