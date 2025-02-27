import re

def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 18, i + 20) if s[i:j] == s[i:j][::-1] and re.fullmatch('[a-z]+', s[i:j])}