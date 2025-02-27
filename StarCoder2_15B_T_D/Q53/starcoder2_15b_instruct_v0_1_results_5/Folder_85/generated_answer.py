import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{85,}\\b'
    palindromes = set()
    for match in re.findall(pattern, string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes