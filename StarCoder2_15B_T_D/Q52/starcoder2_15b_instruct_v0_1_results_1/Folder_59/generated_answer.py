import re

def palindrome_of_length_n(text):
    pattern = re.compile('[a-zA-Z]{39}', re.IGNORECASE)
    matches = pattern.findall(text)
    return set(matches)