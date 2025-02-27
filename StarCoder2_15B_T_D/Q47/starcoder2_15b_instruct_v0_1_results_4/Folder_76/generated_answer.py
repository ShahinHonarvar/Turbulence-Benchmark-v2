import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(154) + ',' + str(182) + '}'
    palindromes = set()
    substring = string[101:293]
    matches = re.finditer(pattern, substring, flags=re.IGNORECASE)
    for match in matches:
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes