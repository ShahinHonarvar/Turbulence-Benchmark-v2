import re

def palindromes_of_specific_lengths(s):
    s = s[:11].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, min(i + 6, len(s) + 1)):
            substring = s[i:j]
            if re.match('^[a-z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes