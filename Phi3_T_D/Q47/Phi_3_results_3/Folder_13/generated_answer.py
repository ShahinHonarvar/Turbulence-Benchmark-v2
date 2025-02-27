import re

def palindromes_of_specific_lengths(s):
    lower_bound, upper_bound = (13, 95)
    valid_lengths = range(57, 61)
    eligible_substring = s[lower_bound:upper_bound + 1]
    palindromes = set()
    for length in valid_lengths:
        for i in range(len(eligible_substring) - length + 1):
            candidate = eligible_substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes