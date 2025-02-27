import re

def palindrome_of_length_n(string):
    pattern = '(?i)([a-z]{37})'
    matches = re.findall(pattern, string)
    return set(matches)