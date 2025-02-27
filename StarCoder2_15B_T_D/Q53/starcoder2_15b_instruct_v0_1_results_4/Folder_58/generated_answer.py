import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{' + str(n) + ',}', re.IGNORECASE)
    palindromes = set(pattern.findall(string))
    return {p for p in palindromes if p == p[::-1]}