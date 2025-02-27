import re

def palindromes_of_specific_lengths(s):
    s = s[15:96].lower()
    return {s[i:j] for i in range(len(s) - 19) for j in range(i + 20, min(i + 67, len(s) + 1)) if s[i:j] == s[i:j][::-1] and re.fullmatch('[a-z]+', s[i:j])}