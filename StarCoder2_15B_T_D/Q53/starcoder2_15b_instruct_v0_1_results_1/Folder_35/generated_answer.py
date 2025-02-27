import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = set(re.findall(pattern, string))
    return {p for p in palindromes if p == p[::-1]}