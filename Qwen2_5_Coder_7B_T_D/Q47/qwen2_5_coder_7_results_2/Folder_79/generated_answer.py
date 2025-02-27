import re

def palindromes_of_specific_lengths(s):
    s = s[1:9]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            substring = s[i:j]
            if re.match('^[A-Za-z]+$', substring) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes