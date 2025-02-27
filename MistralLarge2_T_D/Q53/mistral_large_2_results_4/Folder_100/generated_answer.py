import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 48
    s = re.sub('[^a-zA-Z]', '', s).lower()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes