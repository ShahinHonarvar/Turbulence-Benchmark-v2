import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 14
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes