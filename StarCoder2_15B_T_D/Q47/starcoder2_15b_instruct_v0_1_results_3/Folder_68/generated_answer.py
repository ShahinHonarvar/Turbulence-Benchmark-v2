import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(100) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[:51]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes