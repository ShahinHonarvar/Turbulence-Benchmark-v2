import re

def palindromes_of_specific_lengths(string):
    substring = string[32:72]
    pattern = '[a-zA-Z]{' + str(21) + ',' + str(32) + '}'
    palindromes = set()
    for match in re.finditer(pattern, substring, re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes