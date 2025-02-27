import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{56}', re.IGNORECASE)
    palindromes = set(pattern.findall(string))
    return palindromes