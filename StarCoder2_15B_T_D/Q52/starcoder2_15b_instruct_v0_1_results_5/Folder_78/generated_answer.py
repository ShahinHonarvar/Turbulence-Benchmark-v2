import re

def palindrome_of_length_n(string):
    """
    This function takes a string as input and returns a set of all palindromes of length 48
    as substrings of the given string. Each palindrome should only consist of English letters
    and be found in a case-insensitive manner.
    """
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(48) + '}'
    matches = re.finditer(pattern, string, re.IGNORECASE)
    for match in matches:
        palindrome = match.group()
        palindromes.add(palindrome)
    return palindromes