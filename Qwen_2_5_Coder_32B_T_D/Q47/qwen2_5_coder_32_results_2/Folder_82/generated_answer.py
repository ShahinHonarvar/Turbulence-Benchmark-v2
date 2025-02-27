import re

def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(30, 301):
            substring = s[i:i + j]
            if len(substring) == j and re.match('^[a-z]+$', substring) and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes