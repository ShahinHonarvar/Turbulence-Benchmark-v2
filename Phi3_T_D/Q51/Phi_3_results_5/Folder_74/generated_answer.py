from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_groups[key].append(string)
    anagram_pairs_count = 0
    for group in anagram_groups.values():
        anagram_pairs_count += sum(range(len(group)))
    return anagram_pairs_count <= 57