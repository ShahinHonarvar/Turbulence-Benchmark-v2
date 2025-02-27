import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = re.findall(pattern, string, re.IGNORECASE)
    return set(palindromes)