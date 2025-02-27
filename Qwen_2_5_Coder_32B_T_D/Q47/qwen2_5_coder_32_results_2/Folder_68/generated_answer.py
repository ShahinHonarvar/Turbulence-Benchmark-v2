import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    palindromes = set()
    for i in range(50, 101):
        for start in range(51 - i + 1):
            substring = s[start:start + i]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes