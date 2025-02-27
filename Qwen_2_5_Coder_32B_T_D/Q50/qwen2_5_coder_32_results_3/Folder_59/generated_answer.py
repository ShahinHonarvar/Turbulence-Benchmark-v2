from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            d[sorted_s].append(s_lower)
    anagram_pairs = 0
    for v in d.values():
        anagram_pairs += len(v) * (len(v) - 1) // 2
        if anagram_pairs >= 10:
            return True
    return False