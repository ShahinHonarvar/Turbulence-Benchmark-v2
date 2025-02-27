import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + 20, length + 1):
            substr = s[i:j]
            if substr == substr[::-1] and re.match('^[a-zA-Z]*$', substr):
                palindromes.add(substr)
    return palindromes