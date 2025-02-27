import re

def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    palindromes = set()
    for i in range(len(s) - 25):
        for j in range(i + 25, min(i + 31, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes