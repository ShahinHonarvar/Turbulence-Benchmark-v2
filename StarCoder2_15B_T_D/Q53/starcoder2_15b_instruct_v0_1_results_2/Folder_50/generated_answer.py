import re

def palindrome_of_length_at_least_n(text):
    pattern = '\\b[A-Za-z]{91,}\\b'
    palindromes = set()
    for match in re.findall(pattern, text):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes