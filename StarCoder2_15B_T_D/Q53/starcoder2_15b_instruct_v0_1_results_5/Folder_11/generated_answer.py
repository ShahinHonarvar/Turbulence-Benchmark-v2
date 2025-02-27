import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{54,}\\b'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        match_lowercase = match.lower()
        if match_lowercase == match_lowercase[::-1]:
            palindromes.add(match)
    return palindromes