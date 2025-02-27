from collections import defaultdict
from itertools import combinations

def _sort_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    string_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = _sort_string(string)
            string_map[sorted_string].append(string)
    anagram_pairs = 0
    for strings in string_map.values():
        if len(strings) >= 2:
            anagram_pairs += len(list(combinations(strings, 2)))
    return anagram_pairs >= 24