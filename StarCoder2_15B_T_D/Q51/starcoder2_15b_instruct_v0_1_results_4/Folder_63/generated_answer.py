from typing import List

def if_contains_anagrams(strings: List[str]) -> bool:
    """
    Returns `True` if there are at most 423 pairs of anagrams in `strings`; otherwise, returns `False`.
    Anagrams are considered only for the English letters. Anagrams of length at least three are considered.
    Strings are compared in a case-insensitive manner.
    """
    anagram_groups = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and all((c.isalpha() for c in s)):
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_groups:
                anagram_groups[sorted_s].append(s)
            else:
                anagram_groups[sorted_s] = [s]
    num_pairs = 0
    for group in anagram_groups.values():
        num_pairs += len(group) * (len(group) - 1) // 2
    return num_pairs <= 423