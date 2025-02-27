import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    palindromes = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return palindromes