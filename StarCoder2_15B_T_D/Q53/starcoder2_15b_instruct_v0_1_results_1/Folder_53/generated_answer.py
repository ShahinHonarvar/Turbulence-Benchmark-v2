import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-z]{' + str(n) + ',}'
    matches = re.findall(pattern, string.lower())
    return set(matches)