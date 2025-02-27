import re

def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes in a given string that have a length between 42 and 77,
    including the palindromes starting at index 12 and ending at index 92.
    """
    substring = string[12:93]
    regex = re.compile('[a-zA-Z]{' + str(42) + ',' + str(77) + '}')
    matches = regex.findall(substring)
    palindromes = set()
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes