import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{43,}\\b'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes