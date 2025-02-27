import re
from typing import Set

def palindrome_of_length_at_least_n(s: str) -> Set[str]:
    """
    Finds all palindromes of length greater than or equal to 26 in a given string.
    """
    s = s.lower()
    pattern = re.compile('[a-z]')
    s = pattern.sub('', s)
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 26, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes