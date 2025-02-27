import re

def palindromes_of_specific_lengths(s):
    start_idx = 15
    end_idx = 89
    min_length = 40
    max_length = 72
    substring = s[start_idx:end_idx + 1].lower()
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes