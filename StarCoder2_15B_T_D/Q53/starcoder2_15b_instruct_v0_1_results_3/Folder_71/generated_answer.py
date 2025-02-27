import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(87) + ',}'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    palindromes = set()
    for match in regex.findall(string):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes