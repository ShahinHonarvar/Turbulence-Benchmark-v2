import re

def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    p = re.compile('[a-z]{5,80}')
    matches = p.findall(s)
    palindromes = {m for m in matches if m == m[::-1]}
    return palindromes