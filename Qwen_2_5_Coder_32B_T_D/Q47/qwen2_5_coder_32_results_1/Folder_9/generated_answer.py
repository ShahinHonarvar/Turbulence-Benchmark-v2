import re

def palindromes_of_specific_lengths(s):
    s = s[:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 61, len(s)) + 1):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes