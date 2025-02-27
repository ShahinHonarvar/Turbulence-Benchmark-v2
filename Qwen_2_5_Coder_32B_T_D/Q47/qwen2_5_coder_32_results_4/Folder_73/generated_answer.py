import re

def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 22, min(i + 34, len(s)) + 1):
            substr = s[i:j]
            if re.fullmatch('[a-z]+', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes