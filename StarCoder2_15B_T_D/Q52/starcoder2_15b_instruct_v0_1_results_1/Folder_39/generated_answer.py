import re

def palindrome_of_length_n(string):
    pattern = '\\b[a-zA-Z]{59}\\b'
    palindromes = set()
    for match in re.findall(pattern, string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes