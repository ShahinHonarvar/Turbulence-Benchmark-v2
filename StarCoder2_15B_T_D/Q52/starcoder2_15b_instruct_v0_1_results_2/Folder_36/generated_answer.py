import re

def palindrome_of_length_n(text):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    matches = re.findall(pattern, text, re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes