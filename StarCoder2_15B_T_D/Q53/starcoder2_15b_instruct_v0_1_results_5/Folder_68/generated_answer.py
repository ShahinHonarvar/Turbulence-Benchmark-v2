import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, re.IGNORECASE)
    return set((match for match in matches if match == match[::-1]))