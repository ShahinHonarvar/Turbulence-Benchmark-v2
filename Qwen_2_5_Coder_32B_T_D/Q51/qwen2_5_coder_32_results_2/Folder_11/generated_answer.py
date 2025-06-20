from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in d.values()))
    return anagram_pairs <= 41