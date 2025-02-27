import re

def palindromes_of_specific_lengths(s):
    s = s[30:85].lower()
    regex = re.compile('[a-z]')
    palindromes = set()
    for start in range(len(s) - 11):
        for end in range(start + 11, min(start + 20, len(s)) + 1):
            substring = ''.join(regex.findall(s[start:end]))
            if substring == substring[::-1] and 12 <= len(substring) <= 20:
                palindromes.add(substring)
    return palindromes