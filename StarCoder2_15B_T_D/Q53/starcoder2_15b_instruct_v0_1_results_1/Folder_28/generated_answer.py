import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    results = set()
    for match in matches:
        if match == match[::-1]:
            results.add(match)
    return results