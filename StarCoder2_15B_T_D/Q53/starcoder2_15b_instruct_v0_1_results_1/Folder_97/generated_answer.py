import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    regex = re.compile(pattern, re.IGNORECASE)
    palindromes = regex.findall(string)
    return set(palindromes)