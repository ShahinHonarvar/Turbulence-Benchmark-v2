import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    matches = re.findall('[a-z]{84,}', string)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes