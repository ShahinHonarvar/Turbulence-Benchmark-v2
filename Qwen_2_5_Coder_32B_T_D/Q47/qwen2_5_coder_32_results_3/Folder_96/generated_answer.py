import re

def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    palindromes = set()
    for start in range(len(s) - 49):
        for end in range(start + 49, min(start + 100, len(s))):
            substring = s[start:end + 1]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes