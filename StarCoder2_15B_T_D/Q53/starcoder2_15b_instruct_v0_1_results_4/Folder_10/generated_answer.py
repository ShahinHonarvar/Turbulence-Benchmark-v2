import re

def palindrome_of_length_at_least_n(string):
    regex = re.compile('\\b[a-zA-Z]{92,}\\b')
    matches = regex.findall(string)
    return set(matches)