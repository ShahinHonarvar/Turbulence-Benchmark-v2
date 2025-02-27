import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{40}')
    palindromes = set()
    for match in pattern.findall(string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes