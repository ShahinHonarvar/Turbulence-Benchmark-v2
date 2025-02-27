from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_map[sorted_s].append(s_lower)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_map.values()))
    return anagram_count >= 15