from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            d[key].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values() if len(v) > 1))
    return anagram_pairs >= 61