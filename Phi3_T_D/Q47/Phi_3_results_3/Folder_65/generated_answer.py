import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[15:96]
    for length in range(20, 67):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate.lower())
    return palindromes