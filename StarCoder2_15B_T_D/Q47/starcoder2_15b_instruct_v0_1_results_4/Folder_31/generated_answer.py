import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(37) + ',' + str(60) + '}'
    palindromes = set()
    for match in re.finditer(pattern, s[11:84]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes