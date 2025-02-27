import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(20) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[30:85]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes