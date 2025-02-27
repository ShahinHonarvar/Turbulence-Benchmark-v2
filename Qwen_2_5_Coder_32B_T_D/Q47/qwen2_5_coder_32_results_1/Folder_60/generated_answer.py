import re

def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    return {s[i:i + l] for l in range(32, 35) for i in range(84 - l) if re.match('^[a-z]+$', s[i:i + l]) and s[i:i + l] == s[i:i + l][::-1]}