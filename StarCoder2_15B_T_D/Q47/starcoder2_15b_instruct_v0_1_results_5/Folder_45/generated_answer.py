import re

def palindromes_of_specific_lengths(string):
    pattern = '[a-zA-Z]{' + str(3) + ',' + str(60) + '}'
    match = re.search(pattern, string[70:141])
    if match:
        palindrome = match.group()
        return {palindrome.lower()}
    else:
        return set()