import re

def palindrome_of_length_n(text):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return set(matches)