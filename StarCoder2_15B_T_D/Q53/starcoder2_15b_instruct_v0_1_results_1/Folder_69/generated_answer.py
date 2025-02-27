import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(98) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    return set(filter(lambda x: x == x[::-1], matches))