from typing import List
from itertools import combinations

def if_contains_anagrams(strings: List[str]) -> bool:
    """
    Returns `True` if there are at least 7 pairs of anagrams in `strings`; otherwise, returns `False`.
    Only considers anagrams of length at least 3. Compares strings in a case-insensitive manner.
    """
    anagram_groups = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagram_groups:
                anagram_groups[key].append(s)
            else:
                anagram_groups[key] = [s]
    return sum((len(v) >= 2 for v in anagram_groups.values())) >= 7