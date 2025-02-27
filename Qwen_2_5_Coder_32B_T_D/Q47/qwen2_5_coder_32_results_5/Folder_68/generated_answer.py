import re

def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    palindromes = set()
    for start in range(50):
        for end in range(start + 50, 101):
            if end > len(s):
                break
            substring = s[start:end]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes