import re

def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    palindromes = set()
    for start in range(len(s) - 22):
        for end in range(start + 23, min(start + 40, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and re.fullmatch('[a-z]+', substring):
                palindromes.add(substring)
    return palindromes