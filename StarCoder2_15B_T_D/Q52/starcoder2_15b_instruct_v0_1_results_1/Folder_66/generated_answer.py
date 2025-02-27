import re

def palindrome_of_length_n(string):
    regex = re.compile('[a-zA-Z]{' + str(25) + '}')
    palindromes = set()
    for match in regex.finditer(string):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes