from itertools import permutations
from typing import Set

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> Set[str]:
    s = s[1:9].lower()
    unique_chars = set(s)
    palindrome_set = set()
    minimal_len = 4
    for i in range(1, len(s) + 1):
        for perm in permutations(unique_chars, i):
            if is_palindrome(''.join(perm)):
                palindrome_set.add(''.join(perm))
            if len(perm) >= minimal_len:
                break
    return palindrome_set