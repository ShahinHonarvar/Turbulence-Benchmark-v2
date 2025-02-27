import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    palindromes = set()
    for length in range(50, 101):
        for start in range(51 - length + 1):
            substring = s[start:start + length]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes