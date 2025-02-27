import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{420}', re.IGNORECASE)
    return set(pattern.findall(string))