import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[35:89]
    pattern = '[a-zA-Z]{' + str(24) + ',' + str(33) + '}'
    matches = re.finditer(pattern, substring, re.IGNORECASE)
    for match in matches:
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes