import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[15:73]
    pattern = '[a-zA-Z]{%d,%d}' % (19, 55)
    for match in re.finditer(pattern, substring, re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes