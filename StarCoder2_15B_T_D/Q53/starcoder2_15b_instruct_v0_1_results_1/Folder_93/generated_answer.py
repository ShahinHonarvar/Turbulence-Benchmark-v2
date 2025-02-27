import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(90) + ',}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes