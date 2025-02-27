import re

def palindromes_of_specific_lengths(s):
    """
    Returns the set of all palindromes with the following requirements:
    - Only palindromes occurring in the substring from index 30 to index 84, both inclusive, should be considered.
    - Only palindromes of lengths between 12 to 20 (both inclusive) should be considered.
    - Each palindrome should only consist of English letters.
    - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    - The function should find the palindromes in a case-insensitive manner.
    """
    pattern = '[a-zA-Z]{{12,20}}'
    palindromes = set()
    for match in re.finditer(pattern, s[30:85]):
        palindrome = match.group().lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes