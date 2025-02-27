import re

def palindrome_of_length_at_least_n(string: str) -> set:
    """
    Returns the set of all palindromes of length greater than or equal to 150
    that exist in the given string. Each palindrome should only consist of
    English letters. If no such palindromes exist in the given string,
    the function returns an empty set. The function finds the palindromes
    in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{' + str(150) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes