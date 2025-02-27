import re

def palindrome_of_length_n(string):
    if not string:
        return set()
    regex = re.compile('[a-zA-Z]{93}')
    matches = regex.findall(string)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes