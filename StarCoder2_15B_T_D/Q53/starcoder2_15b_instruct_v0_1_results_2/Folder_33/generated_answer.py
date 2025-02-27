import re

def palindrome_of_length_at_least_n(text):
    regex = re.compile('[a-zA-Z]{141,}')
    matches = regex.findall(text)
    palindromes = [match for match in matches if match == match[::-1]]
    return set(palindromes)