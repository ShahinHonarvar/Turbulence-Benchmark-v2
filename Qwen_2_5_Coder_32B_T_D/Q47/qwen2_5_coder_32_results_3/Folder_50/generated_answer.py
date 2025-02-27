import re

def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 10, min(i + 36, len(s)) + 1):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes