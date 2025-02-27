import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[10:60]
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(36) + '}'
    for match in re.finditer(pattern, substring, flags=re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes