import re

def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes