import re

def palindromes_of_specific_lengths(text):
    """
    Returns a set of all palindromes that satisfy the following conditions:
    1. Only palindromes occurring in the substring from index 18 to index 88, both inclusive, should be considered.
    2. Only palindromes of lengths between 12 to 14 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    regex = re.compile('[a-zA-Z]{12,14}')
    palindromes = set()
    for match in regex.findall(text[18:89]):
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes