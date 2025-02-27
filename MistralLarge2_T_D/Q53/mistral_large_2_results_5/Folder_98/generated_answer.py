import re

def palindrome_of_length_at_least_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    n = 6
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes