import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(392) + '}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set(matches)
    return palindromes