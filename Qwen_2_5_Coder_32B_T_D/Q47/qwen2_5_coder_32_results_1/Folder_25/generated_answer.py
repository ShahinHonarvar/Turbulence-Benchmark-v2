import re

def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 30, min(i + 47, len(s)) + 1) if re.match('^[a-z]+$', s[i:j]) and s[i:j] == s[i:j][::-1]}