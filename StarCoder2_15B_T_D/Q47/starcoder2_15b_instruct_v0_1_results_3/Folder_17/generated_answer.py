import re

def palindromes_of_specific_lengths(text):
    pattern = '[a-zA-Z]{' + str(52) + ',' + str(55) + '}'
    palindromes = set(re.findall(pattern, text[22:96]))
    return palindromes