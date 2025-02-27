import re

def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    p = re.compile('[a-z]{3,6}')
    matches = p.findall(s)
    return {m for m in matches if m == m[::-1]}