import re

def palindromes_of_specific_lengths(string):
    substring = string[13:100]
    pattern = re.compile('[a-zA-Z]{26,29}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes