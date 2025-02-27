import re

def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes