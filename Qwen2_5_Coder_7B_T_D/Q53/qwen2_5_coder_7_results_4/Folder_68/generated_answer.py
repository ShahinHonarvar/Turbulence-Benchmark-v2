import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    words = re.findall('\\\\b[a-z]{2,}\\\\b', s)
    palindromes = set((word for word in words if word == word[::-1] and len(word) >= 21))
    return palindromes