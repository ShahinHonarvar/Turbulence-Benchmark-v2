import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 41, len(s) + 1):
            substring = re.sub('[^a-z]', '', s[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes