import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(109) + ',' + str(126) + '}'
    substring = s[125:284]
    palindromes = set(re.findall(pattern, substring, re.IGNORECASE))
    return palindromes