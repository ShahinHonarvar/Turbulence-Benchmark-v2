import re

def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    palindromes = set()
    for start in range(len(s) - 36):
        for end in range(start + 37, min(start + 61, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes