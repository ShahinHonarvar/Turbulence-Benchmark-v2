import re

def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:66].lower()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result