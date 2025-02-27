import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(318) + '}'
    palindromes = set(re.findall(pattern, string, flags=re.I))
    return palindromes