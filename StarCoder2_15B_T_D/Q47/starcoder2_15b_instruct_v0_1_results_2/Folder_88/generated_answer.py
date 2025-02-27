import re

def palindromes_of_specific_lengths(string):
    pattern = '.{11}(?:(?P<palindrome>[a-zA-Z]{4,5})(?P=palindrome)).{66}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return set(matches)