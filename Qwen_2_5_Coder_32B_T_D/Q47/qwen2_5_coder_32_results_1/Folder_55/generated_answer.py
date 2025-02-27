import re

def palindromes_of_specific_lengths(s):
    s = s[10:76].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 9, min(i + 20, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes