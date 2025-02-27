import re

def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, min(i + 6, len(s)) + 1):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes