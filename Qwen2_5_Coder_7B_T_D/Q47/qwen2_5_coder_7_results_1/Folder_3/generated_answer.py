import re

def palindromes_of_specific_lengths(s):
    substring = s[27:96]
    pattern = re.compile('[a-zA-Z]{49,51}')
    matches = re.findall(pattern, substring, re.IGNORECASE)
    return {m.lower() for m in matches if m == m[::-1]}