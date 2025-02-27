import re

def palindrome_of_length_n(string):
    pattern = '[A-Za-z]{' + str(72) + '}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes