import re

def palindromes_of_specific_lengths(s):
    s = s[24:98].lower()
    palindromes = set()
    for start in range(len(s) - 9):
        for end in range(start + 10, min(start + 37, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes