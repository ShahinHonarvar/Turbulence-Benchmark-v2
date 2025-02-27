import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(16) + ',' + str(39) + '}'
    sub_string = string[16:61]
    palindromes = set()
    for match in re.finditer(pattern, sub_string, flags=re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes