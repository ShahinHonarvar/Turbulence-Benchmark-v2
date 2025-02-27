import re

def palindrome_of_length_at_least_n(string):
    regex = '\\b[a-zA-Z]{59,}\\b'
    palindromes = set()
    for match in re.findall(regex, string, flags=re.IGNORECASE):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes