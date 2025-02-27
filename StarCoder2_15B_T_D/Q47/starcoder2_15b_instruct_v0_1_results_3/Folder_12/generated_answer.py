import re

def palindromes_of_specific_lengths(string):
    substring = string[62:89]
    pattern = '[a-zA-Z]{' + str(18) + ',' + str(21) + '}'
    palindromes = set()
    for match in re.finditer(pattern, substring, flags=re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes