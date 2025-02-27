import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    n = 149
    length = len(s)
    for i in range(length):
        for j in range(i + n, length + 1):
            substr = s[i:j]
            if substr == substr[::-1] and re.match('^[A-Za-z]*$', substr):
                palindromes.add(substr)
    return palindromes