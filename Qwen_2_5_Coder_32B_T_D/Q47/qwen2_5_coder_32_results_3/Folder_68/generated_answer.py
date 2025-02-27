import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    palindromes = set()
    for length in range(50, 101):
        for start in range(52 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and re.match('^[a-z]+$', substring):
                palindromes.add(substring)
    return palindromes