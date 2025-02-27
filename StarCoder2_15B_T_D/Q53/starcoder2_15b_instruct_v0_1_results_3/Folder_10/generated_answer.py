import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(92) + ',}'
    palindromes = re.findall(pattern, string, flags=re.IGNORECASE)
    return set(palindromes)