import re

def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    palindromes = set()
    for i in range(len(s) - 33):
        for j in range(i + 33, min(len(s), i + 54) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes