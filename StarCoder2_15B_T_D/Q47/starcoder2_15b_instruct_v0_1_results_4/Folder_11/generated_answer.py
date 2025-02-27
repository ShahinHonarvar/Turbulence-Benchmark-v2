import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(10) + ',' + str(36) + '}'
    substring = s[24:98]
    palindromes = set(re.findall(pattern, substring, flags=re.IGNORECASE))
    return palindromes