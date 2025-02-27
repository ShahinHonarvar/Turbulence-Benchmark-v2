import re

def palindromes_of_specific_lengths(s):
    s = s[24:85].lower()
    palindromes = set()
    for i in range(len(s) - 21 + 1):
        for j in range(i + 21, min(i + 32, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes