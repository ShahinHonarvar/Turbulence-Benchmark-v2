import re

def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    pattern = re.compile('[a-z]{35,41}')
    matches = pattern.findall(s)
    return {m for m in matches if m == m[::-1]}