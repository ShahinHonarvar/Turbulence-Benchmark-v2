import re

def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 11, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes