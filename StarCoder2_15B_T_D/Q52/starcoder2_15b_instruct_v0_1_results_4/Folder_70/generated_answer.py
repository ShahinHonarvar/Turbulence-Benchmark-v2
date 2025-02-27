import re

def palindrome_of_length_n(s):
    pattern = re.compile('[a-zA-Z]{401}', re.IGNORECASE)
    palindromes = set()
    for match in pattern.findall(s):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes