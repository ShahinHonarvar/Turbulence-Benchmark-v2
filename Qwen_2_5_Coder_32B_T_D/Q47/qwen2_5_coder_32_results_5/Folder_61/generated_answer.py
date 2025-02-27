import re

def palindromes_of_specific_lengths(s):
    s = s[:31].upper()
    return {s[i:j] for i in range(31) for j in range(i + 20, 31) if re.match('^[A-Z]+$', s[i:j]) and s[i:j] == s[i:j][::-1]}