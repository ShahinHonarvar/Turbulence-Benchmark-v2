import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes