import re

def palindrome_of_length_at_least_n(s):
    """
    Finds all palindromes of length greater than or equal to 59 in a given string.
    """
    s = s.lower()
    pattern = '[a-z]{' + str(59) + ',}'
    matches = re.findall(pattern, s)
    palindromes = []
    for match in matches:
        if match == match[::-1]:
            palindromes.append(match)
    return set(palindromes)