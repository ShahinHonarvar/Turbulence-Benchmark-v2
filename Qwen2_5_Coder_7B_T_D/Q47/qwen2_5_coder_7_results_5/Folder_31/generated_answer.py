import re

def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    pattern = re.compile('[a-z]{37,60}')
    matches = pattern.findall(s)
    return {m for m in matches if m == m[::-1]}