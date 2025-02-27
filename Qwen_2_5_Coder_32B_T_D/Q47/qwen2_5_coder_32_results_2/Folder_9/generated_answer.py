import re

def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    palindromes = set()
    for start in range(len(s) - 49):
        for end in range(start + 50, min(start + 61, len(s)) + 1):
            substring = s[start:end]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes