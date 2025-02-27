import re

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    return set(re.findall(pattern, string, re.IGNORECASE))