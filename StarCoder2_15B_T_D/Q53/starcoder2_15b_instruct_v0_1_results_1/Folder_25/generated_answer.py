import re

def palindrome_of_length_at_least_n(text):
    n = 38
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, text)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes