import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pattern = '[a-z]{' + str(n) + ',}'
    matches = re.findall(pattern, string)
    palindromes = []
    for match in matches:
        if match == match[::-1]:
            palindromes.append(match)
    return set(palindromes)