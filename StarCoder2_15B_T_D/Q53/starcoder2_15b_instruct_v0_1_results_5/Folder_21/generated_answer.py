import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{112,}')
    matches = pattern.findall(string)
    return set((match for match in matches if match == match[::-1]))