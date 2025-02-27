import re

def palindrome_of_length_at_least_n(string, n=85):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = set(re.findall(pattern, string, flags=re.IGNORECASE))
    return {word for word in matches if word == word[::-1]}