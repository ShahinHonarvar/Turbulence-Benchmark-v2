import re

def palindromes_of_specific_lengths(s):
    s = s[44:100].lower()
    palindromes = set()
    for start in range(len(s)):
        for length in range(13, 43):
            end = start + length
            if end <= len(s):
                substring = s[start:end]
                if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                    palindromes.add(substring)
    return palindromes