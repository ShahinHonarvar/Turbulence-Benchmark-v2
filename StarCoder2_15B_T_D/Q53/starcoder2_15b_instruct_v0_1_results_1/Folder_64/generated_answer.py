import re

def palindrome_of_length_at_least_n(s):
    """
    Find all palindromes of length greater than or equal to 9 in a given string.
    Only English letters are considered in the palindromes. Case-insensitive.
    """
    regex = '[a-zA-Z]{' + str(n) + ',}'
    palindromes = re.findall(regex, s, flags=re.IGNORECASE)
    return set(palindromes)