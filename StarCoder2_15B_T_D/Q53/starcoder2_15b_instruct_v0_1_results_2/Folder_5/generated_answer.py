import re

def palindrome_of_length_at_least_n(text):
    pattern = '\\b[a-z]{46,}\\b'
    return set(re.findall(pattern, text, flags=re.IGNORECASE))