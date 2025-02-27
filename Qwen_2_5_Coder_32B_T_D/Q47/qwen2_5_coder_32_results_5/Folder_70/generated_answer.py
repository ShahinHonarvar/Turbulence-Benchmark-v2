import re

def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 24, min(i + 53, len(s)) + 1):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes