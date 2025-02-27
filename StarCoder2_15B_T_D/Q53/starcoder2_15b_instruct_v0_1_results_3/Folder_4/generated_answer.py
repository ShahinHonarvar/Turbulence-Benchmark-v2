import re

def palindrome_of_length_at_least_n(string):
    regex_pattern = '[a-zA-Z]{' + str(99) + ',}'
    palindromes = set()
    for match in re.findall(regex_pattern, string):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes