import re

def palindrome_of_length_n(text):
    regex = re.compile('[a-zA-Z]{18}', re.IGNORECASE)
    palindromes = regex.findall(text)
    return set(palindromes)