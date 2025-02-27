import re

def palindrome_of_length_at_least_n(string):
    pattern = '([a-zA-Z]{3,})(\\1)\\b'
    matches = re.findall(pattern, string, re.IGNORECASE)
    return {match[0].lower() for match in matches}