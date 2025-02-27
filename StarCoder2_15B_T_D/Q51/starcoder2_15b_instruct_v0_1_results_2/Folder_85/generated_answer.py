from typing import List

def if_contains_anagrams(words: List[str]) -> bool:
    """
    Checks if the given list of words contains at most 276 pairs of anagrams. Anagrams
    are defined as strings that contain the same letters, regardless of their case. Only
    anagrams of length 3 or greater are considered.
    """
    anagram_groups = {}
    for word in words:
        canonical_form = ''.join(sorted(word.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_groups:
                anagram_groups[canonical_form].append(word)
            else:
                anagram_groups[canonical_form] = [word]
    anagram_pairs = 0
    for group in anagram_groups.values():
        group_size = len(group)
        if group_size >= 2:
            anagram_pairs += group_size * (group_size - 1) // 2
    return anagram_pairs <= 276