from itertools import permutations
from typing import Set

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_between_indices(s: str) -> Set[str]:
    sub_str = s[3:8]
    char_pool = ''.join(set(sub_str.lower()))
    palindromes = set()
    if len(char_pool) < 2:
        return palindromes
    for i in range(4, len(char_pool) + 1):
        for perm in permutations(char_pool, i):
            candidate = ''.join(perm).capitalize() + ''.join(reversed(perm))
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes