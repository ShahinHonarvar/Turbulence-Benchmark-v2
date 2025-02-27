import re

def palindromes_of_specific_lengths(text):
    subtext = text[18:89]
    pattern = '[a-zA-Z]{' + str(12) + ',' + str(14) + '}'
    palindromes = set()
    for match in re.finditer(pattern, subtext, flags=re.IGNORECASE):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes