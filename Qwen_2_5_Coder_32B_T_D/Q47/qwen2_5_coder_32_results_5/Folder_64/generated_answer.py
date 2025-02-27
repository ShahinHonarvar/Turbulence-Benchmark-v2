import re

def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    regex = re.compile('[a-z]{4,5}')
    matches = regex.findall(s)
    return {m for m in matches if m == m[::-1]}