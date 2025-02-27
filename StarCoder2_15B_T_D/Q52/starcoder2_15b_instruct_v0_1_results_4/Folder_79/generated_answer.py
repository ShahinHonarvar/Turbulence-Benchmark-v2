import re

def palindrome_of_length_n(text):
    pattern = '[a-zA-Z]{' + str(n) + '}'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return set([match for match in matches if match == match[::-1]])