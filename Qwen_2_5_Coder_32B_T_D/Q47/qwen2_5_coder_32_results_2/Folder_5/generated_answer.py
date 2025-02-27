import re

def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    return {w for w in re.findall('[a-z]{4,5}', s) if w == w[::-1]}