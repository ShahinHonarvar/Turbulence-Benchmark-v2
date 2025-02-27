from itertools import permutations
from typing import Set

def palindromes_between_indices(s: str) -> Set[str]:
    sub_str = s[2:6]
    sub_str_lower = sub_str.lower()
    unique_chars = set(sub_str_lower)
    valid_permutations = set()
    for i in range(3, len(unique_chars) + 1, 2):
        for perm in permutations(unique_chars, i):
            palindrome_candidate = (''.join(perm) + perm[:-1][::-1]).lower()
            valid_permutations.add(palindrome_candidate)
    return valid_permutations