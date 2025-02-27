from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s].append(s)
    anagram_pairs = 0
    for v in anagram_map.values():
        if len(v) > 1:
            anagram_pairs += len(v) * (len(v) - 1) // 2
    return anagram_pairs >= 16