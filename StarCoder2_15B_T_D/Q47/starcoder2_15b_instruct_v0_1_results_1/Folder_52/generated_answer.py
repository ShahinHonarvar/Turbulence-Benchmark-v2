import re

def palindromes_of_specific_lengths(string):
    substring = string[44:100]
    pattern = re.compile('[a-zA-Z]{13,42}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes