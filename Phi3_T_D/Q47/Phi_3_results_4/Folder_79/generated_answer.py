import re

def palindromes_of_specific_lengths(s):
    sub_string = s[1:9]
    palindromes = set()
    for length in range(3, 5):
        for start in range(len(sub_string) - length + 1):
            candidate = sub_string[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate.lower())
    return palindromes