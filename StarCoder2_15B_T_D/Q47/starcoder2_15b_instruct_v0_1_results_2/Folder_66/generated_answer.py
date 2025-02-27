import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[32:80]
    pattern = '[a-zA-Z]{' + str(35) + ',' + str(41) + '}'
    for match in re.finditer(pattern, substring, re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes