from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_map[normalize(s)].append(s)
    anagram_count = 0
    for _, anagrams in anagram_map.items():
        if len(anagrams) > 1:
            anagram_count += combinations(len(anagrams), 2)
    return anagram_count >= 277