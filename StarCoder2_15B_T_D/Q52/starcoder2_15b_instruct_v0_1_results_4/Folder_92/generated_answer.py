import re

def palindrome_of_length_n(s):
    pattern = re.compile('[a-zA-Z]{10}', re.IGNORECASE)
    return set(pattern.findall(s))