import re

def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 55, min(i + 72, len(s) + 1)) if re.fullmatch('[a-z]+', s[i:j]) and s[i:j] == s[i:j][::-1]}