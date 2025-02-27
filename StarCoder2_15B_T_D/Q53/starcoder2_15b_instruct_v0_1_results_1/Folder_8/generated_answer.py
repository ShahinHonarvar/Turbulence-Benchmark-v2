import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[A-Za-z]{45,}\\b'
    matches = re.findall(pattern, string)
    return set(matches)