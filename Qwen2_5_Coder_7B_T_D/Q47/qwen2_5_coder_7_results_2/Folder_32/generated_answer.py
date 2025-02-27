import re

def palindromes_of_specific_lengths(s):
    substr = s[16:78].lower()
    pattern = re.compile('[a-z]{43,47}')
    matches = pattern.findall(substr)
    palindromes = {m for m in matches if m == m[::-1]}
    return palindromes