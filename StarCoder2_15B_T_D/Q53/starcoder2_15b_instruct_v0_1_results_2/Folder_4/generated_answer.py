import re

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes