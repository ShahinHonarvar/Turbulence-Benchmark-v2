import re

def palindrome_of_length_n(string: str) -> set:
    """
    Finds all palindromes of length 85 in a given string.
    Each palindrome must only consist of English letters.
    """
    patterns = [re.compile(f'(?i)({letter * 85})', re.DOTALL) for letter in string if letter.isalpha()]
    palindromes = set()
    for pattern in patterns:
        matches = pattern.findall(string)
        palindromes.update(matches)
    return palindromes