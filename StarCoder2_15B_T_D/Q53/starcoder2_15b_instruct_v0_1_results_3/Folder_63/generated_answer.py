import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{37,}'
    matches = re.findall(pattern, string)
    palindromes = set()
    for match in matches:
        if match.casefold() == match[::-1].casefold():
            palindromes.add(match)
    return palindromes