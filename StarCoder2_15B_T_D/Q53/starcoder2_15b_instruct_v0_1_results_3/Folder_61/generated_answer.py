import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{5,}'
    matches = re.findall(pattern, string)
    return {match for match in matches if match == match[::-1]}