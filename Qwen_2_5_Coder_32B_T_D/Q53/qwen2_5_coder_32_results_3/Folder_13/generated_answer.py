import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = re.compile('[a-z]{52,}')
    matches = set(regex.findall(s))
    palindromes = {m for m in matches if m == m[::-1]}
    return palindromes