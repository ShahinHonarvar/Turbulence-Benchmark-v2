import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(4) + ',' + str(5) + '}'
    sub_string = string[11:88]
    palindromes = set()
    for match in re.finditer(pattern, sub_string, re.IGNORECASE):
        palindrome = match.group()
        reversed_palindrome = palindrome[::-1]
        if palindrome.lower() == reversed_palindrome.lower():
            palindromes.add(palindrome)
    return palindromes