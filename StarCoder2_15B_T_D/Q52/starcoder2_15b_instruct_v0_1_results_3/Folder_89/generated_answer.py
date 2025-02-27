import re

def palindrome_of_length_n(text):
    text = text.lower()
    pattern = '[a-z]{' + str(n) + '}'
    matches = re.findall(pattern, text)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes