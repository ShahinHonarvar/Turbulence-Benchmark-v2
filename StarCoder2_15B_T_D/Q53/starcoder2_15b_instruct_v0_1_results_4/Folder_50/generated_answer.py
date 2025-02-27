import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = re.findall(pattern, string)
    return set(palindromes)