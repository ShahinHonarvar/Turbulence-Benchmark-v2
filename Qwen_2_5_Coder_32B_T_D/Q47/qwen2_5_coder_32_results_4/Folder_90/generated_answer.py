import re

def palindromes_of_specific_lengths(s):
    s = s[106:281].lower()
    return {s[i:i + l] for l in range(136, 152) for i in range(len(s) - l + 1) if re.match('^[a-z]+$', s[i:i + l]) and s[i:i + l] == s[i:i + l][::-1]}