import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(18) + '}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes