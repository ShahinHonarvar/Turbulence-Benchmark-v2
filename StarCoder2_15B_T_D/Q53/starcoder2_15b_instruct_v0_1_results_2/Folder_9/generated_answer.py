import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{{95,}}'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes