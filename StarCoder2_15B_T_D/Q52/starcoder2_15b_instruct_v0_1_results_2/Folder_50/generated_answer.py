import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(40) + '}'
    for match in re.finditer(pattern, string, flags=re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes