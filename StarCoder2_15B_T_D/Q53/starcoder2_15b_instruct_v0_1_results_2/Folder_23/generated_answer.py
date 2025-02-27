import re

def palindrome_of_length_at_least_n(string):
    pattern = '(?i)(?:\\w{19,})(?:\\w{19,})'
    matches = re.findall(pattern, string)
    palindromes = set(matches)
    return palindromes