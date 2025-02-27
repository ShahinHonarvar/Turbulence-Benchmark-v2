import re

def palindromes_of_specific_lengths(string):
    substring = string[200:301]
    regex = '\\\\b[A-Za-z]{' + str(10) + ',' + str(50) + '}\\\\b'
    palindromes = set()
    for match in re.finditer(regex, substring, flags=re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes