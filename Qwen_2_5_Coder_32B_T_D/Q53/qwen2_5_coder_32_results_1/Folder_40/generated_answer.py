import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 2, n + 1):
            candidate = s[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes