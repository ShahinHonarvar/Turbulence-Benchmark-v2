import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '[a-z]{' + str(18) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes