import re

def palindromes_of_specific_lengths(s):
    s = s[35:89].lower()
    palindromes = set()
    for i in range(len(s) - 23):
        for j in range(i + 24, min(i + 34, len(s)) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes