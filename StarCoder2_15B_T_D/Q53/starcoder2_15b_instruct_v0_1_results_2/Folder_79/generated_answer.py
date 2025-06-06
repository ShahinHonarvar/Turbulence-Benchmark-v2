import re

def palindrome_of_length_at_least_n(string):
    pattern = '[A-Za-z]{' + str(n) + ',}'
    palindromes = set()
    for match in re.findall(pattern, string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes