import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    for match in re.findall(pattern, string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes