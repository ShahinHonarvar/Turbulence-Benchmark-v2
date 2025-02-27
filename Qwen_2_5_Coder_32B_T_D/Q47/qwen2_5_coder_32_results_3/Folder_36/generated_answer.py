import re

def palindromes_of_specific_lengths(s):
    s = s[124:284].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 115, min(i + 135, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes