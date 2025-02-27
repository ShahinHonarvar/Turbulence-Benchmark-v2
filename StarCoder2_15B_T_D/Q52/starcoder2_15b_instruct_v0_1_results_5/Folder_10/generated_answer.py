import re

def palindrome_of_length_n(string):
    regex = '[a-zA-Z]{' + str(n) + '}'
    palindromes = set(re.findall(regex, string, flags=re.I))
    return palindromes