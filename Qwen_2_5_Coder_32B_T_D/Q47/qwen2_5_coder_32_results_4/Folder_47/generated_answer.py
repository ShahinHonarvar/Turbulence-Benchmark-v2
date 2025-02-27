import re

def palindromes_of_specific_lengths(s):
    s = s[39:95].lower()
    palindromes = set()
    for start in range(len(s) - 13):
        for end in range(start + 14, min(start + 53, len(s)) + 1):
            substring = s[start:end]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes