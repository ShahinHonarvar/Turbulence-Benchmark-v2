import re

def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    palindromes = set()
    for start in range(len(s) - 11):
        for end in range(start + 11, min(start + 221, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes