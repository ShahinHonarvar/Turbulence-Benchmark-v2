import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{22,}')
    matches = pattern.findall(string)
    return set((s for s in matches if s.lower() == s[::-1]))