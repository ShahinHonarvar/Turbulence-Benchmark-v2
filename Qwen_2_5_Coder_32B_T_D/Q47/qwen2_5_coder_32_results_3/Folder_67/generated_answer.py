import re

def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    palindromes = set()
    for start in range(len(s) - 26 + 1):
        for end in range(start + 25, min(start + 33, len(s))):
            substring = s[start:end + 1]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes