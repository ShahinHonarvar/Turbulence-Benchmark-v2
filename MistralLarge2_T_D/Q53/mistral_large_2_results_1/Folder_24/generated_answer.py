import re

def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    substrs = set(re.findall('\\b[a-zA-Z]{53,}\\b', s, re.IGNORECASE))
    return set(filter(is_palindrome, substrs))