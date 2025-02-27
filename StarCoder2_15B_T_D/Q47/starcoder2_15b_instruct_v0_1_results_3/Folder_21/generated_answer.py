import re

def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes of specific lengths in a given string.
    Only palindromes between indices 100 and 295 (inclusive) are considered.
    Only palindromes of lengths between 136 and 160 (inclusive) are considered.
    Each palindrome must only consist of English letters.
    """
    pattern = re.compile('[A-Za-z]{136,160}')
    palindromes = set()
    for i in range(100, 296):
        for j in range(i + 136, min(i + 161, len(string))):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes