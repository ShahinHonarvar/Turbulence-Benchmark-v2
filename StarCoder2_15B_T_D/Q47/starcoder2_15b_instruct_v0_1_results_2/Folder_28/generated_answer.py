import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(21) + ',' + str(32) + '}'
    substring = string[32:72]
    palindromes = re.findall(pattern, substring, flags=re.IGNORECASE)
    return set(palindromes)