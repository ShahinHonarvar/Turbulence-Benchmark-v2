import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    pattern = '\\b[a-z]{6,}\\b'
    matches = re.findall(pattern, s)
    palindromes = [word for word in matches if word == word[::-1]]
    return set(palindromes)