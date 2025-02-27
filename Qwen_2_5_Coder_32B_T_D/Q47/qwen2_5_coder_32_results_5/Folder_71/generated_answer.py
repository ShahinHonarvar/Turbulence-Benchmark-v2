import re

def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    palindromes = set()
    for start in range(len(s) - 22):
        for length in range(23, 37):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes