import re

def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    matches = re.findall('[a-z]{3,4}', s)
    return {m for m in matches if m == m[::-1]}