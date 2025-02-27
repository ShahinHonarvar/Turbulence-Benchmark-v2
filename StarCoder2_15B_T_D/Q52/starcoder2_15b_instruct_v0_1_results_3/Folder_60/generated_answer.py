import re

def palindrome_of_length_n(string):
    pattern = '.{88}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = []
    for match in matches:
        if match == match[::-1]:
            palindromes.append(match)
    return set(palindromes)