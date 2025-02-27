import re

def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    palindromes = set()
    for length in range(55, 72):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if re.fullmatch('[a-z]+', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes