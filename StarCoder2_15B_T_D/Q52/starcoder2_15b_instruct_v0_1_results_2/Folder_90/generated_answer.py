import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(n) + '}'
    for match in re.finditer(pattern, string):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes