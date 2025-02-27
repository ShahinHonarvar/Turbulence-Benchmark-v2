import re

def palindromes_of_specific_lengths(s):
    s = s[11:97].lower()
    palindromes = set()
    for i in range(len(s) - 44):
        for j in range(i + 45, min(i + 53, len(s)) + 1):
            substring = s[i:j]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes