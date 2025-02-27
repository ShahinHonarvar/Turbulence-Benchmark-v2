import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '\\b[a-zA-Z]{90,}\\b'
    matches = re.findall(pattern, string)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes