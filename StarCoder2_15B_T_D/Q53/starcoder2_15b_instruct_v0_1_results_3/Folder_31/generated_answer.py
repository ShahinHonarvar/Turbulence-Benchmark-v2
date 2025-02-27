import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = re.compile('[a-z]{34,}')
    matches = pattern.findall(string)
    return set(matches)