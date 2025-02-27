from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_count[sorted_s] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pair_count >= 246