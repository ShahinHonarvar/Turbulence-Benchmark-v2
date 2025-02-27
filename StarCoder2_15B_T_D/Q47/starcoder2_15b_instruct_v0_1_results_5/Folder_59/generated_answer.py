import re

def palindromes_of_specific_lengths(string):
    pattern = re.compile('[a-zA-Z]{3,15}')
    palindromes = set()
    for match in pattern.finditer(string[:101]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes