from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            d[s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values() if len(v) >= 2))
    return anagram_pairs >= 38