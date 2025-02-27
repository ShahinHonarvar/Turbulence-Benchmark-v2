import re

def palindromes_of_specific_lengths(text):
    """
    Returns the set of all palindromes that occur in the substring from index 0 to index 50,
    both inclusive, and have lengths between 50 and 100 (both inclusive), in a case-insensitive
    manner. If no such palindrome occurs, an empty set is returned.
    """
    pattern = '[a-zA-Z]{' + str(50) + ',' + str(100) + '}'
    palindromes = set()
    for match in re.findall(pattern, text[:51]):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes