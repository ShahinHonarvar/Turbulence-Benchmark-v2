import re

def palindrome_of_length_at_least_n(s):
    pattern = '\\b[a-zA-Z]{16,}\\b'
    palindromes = set()
    for match in re.findall(pattern, s, flags=re.IGNORECASE):
        if match.lower() == match[::-1]:
            palindromes.add(match)
    return palindromes