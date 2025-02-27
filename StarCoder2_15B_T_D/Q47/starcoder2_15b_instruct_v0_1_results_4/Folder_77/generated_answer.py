import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[103:277]
    pattern = re.compile('[a-zA-Z]{100,170}')
    for match in pattern.finditer(substring):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes