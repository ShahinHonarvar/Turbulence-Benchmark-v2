import re

def palindromes_of_specific_lengths(s):
    s = s[39:95].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 14, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes