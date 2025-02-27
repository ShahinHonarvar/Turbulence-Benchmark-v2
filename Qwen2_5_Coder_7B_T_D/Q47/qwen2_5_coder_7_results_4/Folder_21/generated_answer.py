import re

def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for length in range(136, 161):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes