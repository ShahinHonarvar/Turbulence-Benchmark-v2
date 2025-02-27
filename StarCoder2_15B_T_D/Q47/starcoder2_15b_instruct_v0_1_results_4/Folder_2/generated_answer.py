import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(36) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[10:60]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes