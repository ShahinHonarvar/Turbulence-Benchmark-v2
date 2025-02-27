import re

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    regex = re.compile('[a-z]{7,}')
    matches = regex.findall(s)
    palindromes = {match for match in matches if match == match[::-1]}
    return palindromes