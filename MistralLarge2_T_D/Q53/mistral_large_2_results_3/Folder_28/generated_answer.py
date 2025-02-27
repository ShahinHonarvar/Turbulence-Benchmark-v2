import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = len(s)
    for length in range(42, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes