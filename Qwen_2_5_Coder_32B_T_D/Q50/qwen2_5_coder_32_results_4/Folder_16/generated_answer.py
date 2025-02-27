from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = tuple(sorted(s_lower))
            d[sorted_s].append(s_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return anagram_pairs >= 155