import re

def palindrome_of_length_n(text):
    pattern = re.compile('[a-zA-Z]{46}')
    palindromes = set()
    for match in pattern.findall(text):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes