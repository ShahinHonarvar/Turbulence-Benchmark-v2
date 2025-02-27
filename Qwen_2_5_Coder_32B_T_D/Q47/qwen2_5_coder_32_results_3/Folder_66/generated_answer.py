import re

def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    palindromes = set()
    for i in range(len(s) - 34):
        for j in range(i + 34, min(i + 42, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes