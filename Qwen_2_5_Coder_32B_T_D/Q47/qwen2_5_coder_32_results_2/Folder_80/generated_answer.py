import re

def palindromes_of_specific_lengths(s):
    s = s[35:89].lower()
    return {s[i:j] for i in range(len(s) - 23) for j in range(i + 24, min(i + 34, len(s) + 1)) if re.fullmatch('[a-z]+', s[i:j]) and s[i:j] == s[i:j][::-1]}