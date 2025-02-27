import re

def palindromes_of_specific_lengths(s):
    s = s[70:141].lower()
    palindromes = set()
    for length in range(3, 61):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes