import re

def palindrome_of_length_at_least_n(string):
    regex = re.compile('[A-Za-z]{77,}')
    palindromes = set()
    for match in regex.findall(string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes