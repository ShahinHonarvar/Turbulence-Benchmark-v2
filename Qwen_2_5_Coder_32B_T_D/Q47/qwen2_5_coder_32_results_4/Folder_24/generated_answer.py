import re

def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 42, min(i + 78, len(s) + 1)) if re.fullmatch('[a-z]+', s[i:j]) and s[i:j] == s[i:j][::-1]}