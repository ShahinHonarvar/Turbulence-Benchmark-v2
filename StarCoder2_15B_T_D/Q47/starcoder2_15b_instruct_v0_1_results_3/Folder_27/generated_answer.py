import re

def palindromes_of_specific_lengths(string):
    substring = string[13:100]
    pattern = '[a-zA-Z]{' + str(26) + ',' + str(29) + '}'
    palindromes = set()
    for match in re.finditer(pattern, substring, flags=re.IGNORECASE):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes