import re

def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for j in range(i + 43, min(i + 48, len(s)) + 1):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes