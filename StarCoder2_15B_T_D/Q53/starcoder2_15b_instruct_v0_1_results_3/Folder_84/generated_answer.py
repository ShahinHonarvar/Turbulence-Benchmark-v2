import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = set(re.findall(pattern, string))
    return palindromes