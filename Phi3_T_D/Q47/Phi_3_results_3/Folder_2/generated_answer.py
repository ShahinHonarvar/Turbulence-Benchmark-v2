import re

def palindromes_of_specific_lengths(s):
    substring = s[10:60]
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if re.match('^[A-Za-z]+$', candidate) and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes