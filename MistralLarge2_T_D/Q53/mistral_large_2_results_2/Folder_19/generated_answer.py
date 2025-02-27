import re

def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    palindromes = set()
    length = len(s_lower)
    for i in range(length):
        for j in range(i + 23, length + 1):
            substr = s_lower[i:j]
            if substr == substr[::-1] and re.match('^[a-z]+$', substr):
                palindromes.add(substr)
    return palindromes