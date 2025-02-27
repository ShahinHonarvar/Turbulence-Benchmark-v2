import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{25,}')
    for match in pattern.findall(text):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes