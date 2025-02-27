import re

def palindromes_of_specific_lengths(string):
    regex = re.compile('[a-zA-Z]{24,52}')
    palindromes = set()
    for match in regex.finditer(string[10:71]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes