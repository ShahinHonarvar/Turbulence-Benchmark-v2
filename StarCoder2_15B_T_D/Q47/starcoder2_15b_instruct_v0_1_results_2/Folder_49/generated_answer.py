import re

def palindromes_of_specific_lengths(string):
    """
    This function takes a string as an argument and returns a set of all palindromes
    that satisfy the following conditions:
    1. Only palindromes occurring in the substring from index 10 to 100, both inclusive, should be considered.
    2. Only palindromes of lengths between 10 to 50 (both inclusive) should be considered.
    3. Each palindrome should only consist of English letters.
    4. If no such palindrome with the specified length occurs in the specified index range, the function should return an empty set.
    5. The function should find the palindromes in a case-insensitive manner.
    """
    pattern = re.compile('[a-zA-Z]{10,50}')
    palindromes = set()
    for match in pattern.finditer(string[10:101]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes