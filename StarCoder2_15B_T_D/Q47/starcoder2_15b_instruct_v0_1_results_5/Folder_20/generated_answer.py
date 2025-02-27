import re

def palindromes_of_specific_lengths(string):
    """
    Finds palindromes of specific lengths in a given string.
    """
    palindromes = set()
    substring = string[20:75]
    pattern = '[a-zA-Z]{' + str(36) + ',' + str(42) + '}'
    matches = re.finditer(pattern, substring, re.IGNORECASE)
    for match in matches:
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes