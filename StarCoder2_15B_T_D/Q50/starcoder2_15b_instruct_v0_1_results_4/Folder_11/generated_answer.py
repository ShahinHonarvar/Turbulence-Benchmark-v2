import itertools
from collections import defaultdict

def if_contains_anagrams(strings):
    """
    Checks if there are at least 28 pairs of anagrams in the given list of strings.
    """
    anagrams = defaultdict(list)
    for string in strings:
        key = tuple(sorted(string.lower()))
        anagrams[key].append(string)
    pairs = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 3:
            pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return pairs >= 28