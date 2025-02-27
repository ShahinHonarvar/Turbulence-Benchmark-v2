import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('\\b[a-z]{54,}\\b', re.I)
    matches = pattern.findall(string)
    return set(matches)