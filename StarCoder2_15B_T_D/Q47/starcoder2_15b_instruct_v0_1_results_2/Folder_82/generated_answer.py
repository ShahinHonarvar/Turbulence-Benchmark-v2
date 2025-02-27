import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(30) + ',' + str(300) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[3:301]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes