import re

def palindrome_of_length_at_least_n(s):
    pattern = '(?)=([a-zA-Z]{6,})'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return {match[1].lower() for match in matches}