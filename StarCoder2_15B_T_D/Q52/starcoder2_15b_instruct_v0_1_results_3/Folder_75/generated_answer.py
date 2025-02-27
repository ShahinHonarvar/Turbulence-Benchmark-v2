import re

def palindrome_of_length_n(s):
    pattern = '[A-Za-z]{' + str(n) + '}'
    palindromes = set(re.findall(pattern, s, re.IGNORECASE))
    return palindromes