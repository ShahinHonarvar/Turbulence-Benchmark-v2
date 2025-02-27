import re

def palindromes_of_specific_lengths(s):
    s = s[130:296]
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 102, min(start + 158, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes