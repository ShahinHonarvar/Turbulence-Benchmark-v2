import re

def palindromes_of_specific_lengths(s):
    s = s[24:85].lower()
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i + 20, min(i + 31, len(s)) + 1):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes