import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[29:99].lower()
    for i in range(len(substring) - 5):
        for j in range(i + 6, min(i + 10, len(substring)) + 1):
            candidate = substring[i:j]
            if re.match('^[a-z]+$', candidate) and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes