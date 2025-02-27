import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[16:61].lower()
    for length in range(16, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes