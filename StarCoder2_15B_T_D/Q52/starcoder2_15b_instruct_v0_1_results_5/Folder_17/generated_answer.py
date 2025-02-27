import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{289}', re.IGNORECASE)
    matches = set()
    for match in pattern.findall(string):
        if match == match[::-1]:
            matches.add(match)
    return matches