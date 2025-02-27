import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string)
    result = set()
    for match in matches:
        if match == match[::-1]:
            result.add(match)
    return result