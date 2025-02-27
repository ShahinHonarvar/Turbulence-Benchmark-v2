import re

def palindromes_of_specific_lengths(s):
    s = s[125:284].lower()
    palindromes = set()
    for start in range(len(s) - 108):
        for end in range(start + 109, min(start + 127, len(s)) + 1):
            substring = s[start:end]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes