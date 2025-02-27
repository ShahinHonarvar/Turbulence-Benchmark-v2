import re

def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes of specific lengths in a given string.
    """
    substring = string[10:56]
    pattern = re.compile('[a-zA-Z]{3,7}')
    palindromes = set()
    for match in pattern.finditer(substring):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes