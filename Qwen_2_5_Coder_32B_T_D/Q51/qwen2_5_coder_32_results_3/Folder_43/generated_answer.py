from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            d[sorted_s].append(s_lower)
    anagram_pairs = sum((1 for l in d.values() if len(l) > 1))
    return anagram_pairs <= 3