import re

def palindrome_of_length_at_least_n(string):
    regex = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = re.findall(regex, string, flags=re.IGNORECASE)
    return set(palindromes)