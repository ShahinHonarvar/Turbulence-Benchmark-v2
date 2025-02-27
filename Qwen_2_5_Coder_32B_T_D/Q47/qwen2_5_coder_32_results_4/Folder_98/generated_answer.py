import re

def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 5, min(start + 81, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes