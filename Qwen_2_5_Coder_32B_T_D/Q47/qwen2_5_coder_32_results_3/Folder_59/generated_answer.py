import re

def palindromes_of_specific_lengths(s):
    s = s[:101].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 16, len(s) + 1)):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes