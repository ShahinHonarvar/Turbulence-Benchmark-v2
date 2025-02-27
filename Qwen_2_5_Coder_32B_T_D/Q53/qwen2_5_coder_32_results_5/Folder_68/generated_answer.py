import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        for j in range(i + 21, len(s) + 1):
            substring = re.sub('[^a-z]', '', s[i:j])
            if substring == substring[::-1] and len(substring) >= 21:
                palindromes.add(substring)
    return palindromes