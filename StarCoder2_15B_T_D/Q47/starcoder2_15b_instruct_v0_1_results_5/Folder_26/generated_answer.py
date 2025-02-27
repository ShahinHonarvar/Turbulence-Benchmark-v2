import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(21) + ',' + str(31) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[24:85]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes