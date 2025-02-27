import re

def palindromes_of_specific_lengths(s: str) -> set:
    """
    Returns the set of all palindromes of lengths between 3 and 6 (both inclusive)
    that occur in the substring from index 0 to index 6, both inclusive, of the given
    string `s`. Each palindrome should only consist of English letters. The palindromes
    are found in a case-insensitive manner.
    """
    palindromes = set()
    s = s[:7].lower()
    for length in range(3, 7):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes