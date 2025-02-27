import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:51]
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(100) + '}'
    matches = re.finditer(pattern, substring, flags=re.IGNORECASE)
    for match in matches:
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes