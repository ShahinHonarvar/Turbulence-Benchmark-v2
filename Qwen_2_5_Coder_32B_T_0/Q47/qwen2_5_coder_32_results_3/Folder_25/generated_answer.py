import re

def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    palindromes = set()
    for i in range(len(s) - 29):
        for j in range(i + 30, min(i + 47, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes