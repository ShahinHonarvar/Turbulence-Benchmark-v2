import re

def palindromes_of_specific_lengths(s):
    pattern = '[a-zA-Z]{' + str(17) + ',' + str(66) + '}'
    palindromes = set()
    for match in re.finditer(pattern, s[12:93]):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes