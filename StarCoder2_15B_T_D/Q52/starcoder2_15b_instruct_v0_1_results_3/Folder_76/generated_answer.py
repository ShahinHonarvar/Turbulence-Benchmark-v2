import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{257}', re.IGNORECASE)
    return set(pattern.findall(string))