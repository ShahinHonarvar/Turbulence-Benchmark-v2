import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    palindromes = set(matches)
    return palindromes