import re

def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    palindromes = set()
    for start in range(len(s) - 51):
        for length in range(52, 57):
            if start + length <= len(s):
                substr = s[start:start + length]
                if substr == substr[::-1] and re.fullmatch('[a-z]+', substr):
                    palindromes.add(substr)
    return palindromes