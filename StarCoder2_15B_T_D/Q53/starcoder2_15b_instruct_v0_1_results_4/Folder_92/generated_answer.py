import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = '[a-z]{' + str(10) + ',}'
    palindromes = set()
    for match in re.findall(pattern, string):
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes