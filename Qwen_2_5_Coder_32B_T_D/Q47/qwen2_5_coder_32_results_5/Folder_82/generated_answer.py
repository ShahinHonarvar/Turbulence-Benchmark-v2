import re

def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 30, 301):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes