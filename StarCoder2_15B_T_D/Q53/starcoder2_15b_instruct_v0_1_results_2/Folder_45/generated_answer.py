import re

def palindrome_of_length_at_least_n(s):
    pattern = '\\b[a-zA-Z]{47,}\\b'
    matches = re.findall(pattern, s)
    return set(matches)