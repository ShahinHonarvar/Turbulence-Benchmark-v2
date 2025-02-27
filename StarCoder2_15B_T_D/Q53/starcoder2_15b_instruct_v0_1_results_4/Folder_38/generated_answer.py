import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return {p for p in palindromes if p == p[::-1]}