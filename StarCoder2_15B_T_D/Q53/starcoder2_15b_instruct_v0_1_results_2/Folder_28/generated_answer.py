import re

def palindrome_of_length_at_least_n(string: str) -> set:
    pattern = re.compile('\\b[a-z]{42,}\\b')
    palindromes = pattern.findall(string.lower())
    palindromes = [p for p in palindromes if p == p[::-1]]
    return set(palindromes)