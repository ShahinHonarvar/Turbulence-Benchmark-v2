import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    pattern = '[a-z]{' + str(42) + ',}'
    for match in re.findall(pattern, string):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes