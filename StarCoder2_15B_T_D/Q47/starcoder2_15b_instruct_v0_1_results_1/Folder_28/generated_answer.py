import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(21) + ',' + str(32) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string[32:72]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes