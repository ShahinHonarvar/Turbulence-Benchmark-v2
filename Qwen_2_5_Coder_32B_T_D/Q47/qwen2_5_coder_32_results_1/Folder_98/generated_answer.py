import re

def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    regex = re.compile('[a-z]')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 4, min(i + 81, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and all((regex.match(char) for char in substring)):
                palindromes.add(substring)
    return palindromes