import re

def palindromes_of_specific_lengths(string):
    """Returns the set of all palindromes with the specified requirements."""
    substring = string[13:96]
    regex_pattern = '[a-zA-Z]{' + str(57) + ',' + str(60) + '}'
    palindromes = set()
    for match in re.finditer(regex_pattern, substring, re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes