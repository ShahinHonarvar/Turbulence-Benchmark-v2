import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{6}', re.I)
    return set(pattern.findall(string))