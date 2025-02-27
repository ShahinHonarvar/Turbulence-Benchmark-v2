import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('(?i)(?)(?{23,38})(?[a-zA-Z]+)(?41,89)')
    palindromes = pattern.findall(string)
    return set(palindromes)