from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            s = ''.join(sorted(s))
            d[s].append(s)
    anagram_pairs = 0
    for k, v in d.items():
        if len(v) > 1:
            anagram_pairs += len(v) * (len(v) - 1) // 2
    return anagram_pairs >= 16