import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{276}')
    return set(pattern.findall(string))