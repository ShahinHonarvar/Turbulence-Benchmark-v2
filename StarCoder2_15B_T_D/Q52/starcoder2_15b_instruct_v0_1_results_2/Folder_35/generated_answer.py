import re

def palindrome_of_length_n(string):
    pattern = re.compile('\\b[a-zA-Z]{116}\\b', re.I)
    return set(pattern.findall(string))