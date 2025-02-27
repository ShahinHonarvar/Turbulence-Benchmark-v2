import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{99,}\\b'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes