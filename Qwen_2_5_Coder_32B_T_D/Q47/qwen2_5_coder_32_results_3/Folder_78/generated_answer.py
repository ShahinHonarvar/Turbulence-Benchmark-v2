import re

def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    palindromes = set()
    for start in range(len(s) - 18):
        for end in range(start + 18, min(start + 55, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes