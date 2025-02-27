from collections import defaultdict

def if_contains_anagrams(lst):
    count_map = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            count_map[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count_map.values() if v > 1))
    return anagram_pairs >= 276