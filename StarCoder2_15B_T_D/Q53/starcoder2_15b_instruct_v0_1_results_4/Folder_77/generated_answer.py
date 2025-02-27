import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '\\b[a-zA-Z]{149,}\\b'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes