import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = re.compile('[a-z]{73,}')
    matches = set(regex.findall(s))
    return {m for m in matches if m == m[::-1]}