import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{29,}'
    matches = re.findall(pattern, string)
    palindromes = [match for match in matches if match == match[::-1]]
    return set(palindromes)