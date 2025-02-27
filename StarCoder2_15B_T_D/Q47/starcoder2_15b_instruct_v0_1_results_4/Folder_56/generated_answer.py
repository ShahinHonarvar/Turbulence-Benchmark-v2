import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(7) + '}'
    palindromes = re.findall(pattern, string[1:10], flags=re.IGNORECASE)
    return set(palindromes)