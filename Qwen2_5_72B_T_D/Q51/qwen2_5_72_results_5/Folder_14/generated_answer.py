from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s] += 1
    pairs = 0
    for count in anagram_map.values():
        pairs += count * (count - 1) // 2
    return pairs <= 474