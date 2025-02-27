import re

def palindromes_of_specific_lengths(s):
    s = s[16:95].lower()
    palindromes = set()
    for start in range(len(s) - 38):
        for end in range(start + 39, min(start + 53, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes