from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            d[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in d.values() if v > 1))
    return anagram_pairs >= 94