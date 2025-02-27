import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '\\b[A-Za-z]{64,}\\b'
    for match in re.findall(pattern, string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes