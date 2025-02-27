import re

def palindrome_of_length_n(text, n):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    palindromes = set(re.findall(pattern, text, flags=re.IGNORECASE))
    return palindromes