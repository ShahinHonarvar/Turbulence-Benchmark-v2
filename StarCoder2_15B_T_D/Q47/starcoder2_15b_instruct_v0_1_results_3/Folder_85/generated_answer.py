import re

def palindromes_of_specific_lengths(string):
    """
    Returns a set of palindromes with lengths between 6 and 9 in the substring from index 29 to 98.
    """
    pattern = re.compile('[a-zA-Z]{6,9}')
    palindromes = set()
    substring = string[29:99]
    matches = pattern.finditer(substring)
    for match in matches:
        word = match.group()
        if word.lower() == word[::-1].lower():
            palindromes.add(word)
    return palindromes