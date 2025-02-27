from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            d[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = [v for v in d.values() if len(v) > 1]
    return sum((len(v) * (len(v) - 1) // 2 for v in anagram_pairs)) >= 50