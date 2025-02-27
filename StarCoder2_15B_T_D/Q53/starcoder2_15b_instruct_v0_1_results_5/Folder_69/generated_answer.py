import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-z]{' + str(98) + ',}'
    matches = re.findall(pattern, string.lower())
    palindromes = [match for match in matches if match == match[::-1]]
    return set(palindromes)