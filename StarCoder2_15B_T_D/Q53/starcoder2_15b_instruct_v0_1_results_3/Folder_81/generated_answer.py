import re

def palindrome_of_length_at_least_n(text):
    pattern = '[a-zA-Z]{33,}'
    matches = re.findall(pattern, text)
    return set([match.lower() for match in matches])