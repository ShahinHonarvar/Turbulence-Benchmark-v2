import re

def palindrome_of_length_n(s):
    pattern = '\\b[a-zA-Z]{66}\\b'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return set(matches)