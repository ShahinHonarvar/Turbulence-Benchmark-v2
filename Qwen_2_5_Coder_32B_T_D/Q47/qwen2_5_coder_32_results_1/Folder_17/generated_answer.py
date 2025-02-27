import re

def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    p = {s[i:i + L] for L in range(52, 56) for i in range(97 - L) if re.fullmatch('[a-z]+', s[i:i + L]) and s[i:i + L] == s[i:i + L][::-1]}
    return p