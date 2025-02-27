import re

def palindrome_of_length_at_least_n(text):
    pattern = '\\b[A-Za-z]{30,}\\b'
    matches = re.findall(pattern, text)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes