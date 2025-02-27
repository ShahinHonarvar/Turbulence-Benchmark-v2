import re

def palindrome_of_length_n(string):
    pattern = re.compile('[A-Za-z]{9}', re.IGNORECASE)
    return set(pattern.findall(string))