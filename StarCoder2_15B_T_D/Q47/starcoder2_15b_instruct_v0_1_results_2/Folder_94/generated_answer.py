import re

def palindromes_of_specific_lengths(text):
    subtext = text[40:95]
    pattern = '[a-zA-Z]{' + str(45) + ',' + str(51) + '}'
    palindromes = set()
    for match in re.finditer(pattern, subtext):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes