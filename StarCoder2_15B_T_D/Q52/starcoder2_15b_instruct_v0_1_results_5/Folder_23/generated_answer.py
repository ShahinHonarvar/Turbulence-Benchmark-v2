import re

def palindrome_of_length_n(string):
    regex = re.compile('[a-zA-Z]{69}', re.IGNORECASE)
    return set(regex.findall(string))