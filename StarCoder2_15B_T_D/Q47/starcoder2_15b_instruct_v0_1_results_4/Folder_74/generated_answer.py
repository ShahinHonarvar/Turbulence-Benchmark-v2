import re

def palindromes_of_specific_lengths(string):
    substring = string[30:85]
    pattern = re.compile('[a-zA-Z]{12,20}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes