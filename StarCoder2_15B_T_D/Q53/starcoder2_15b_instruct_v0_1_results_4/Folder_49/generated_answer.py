import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{73,}\\b'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return set(matches)