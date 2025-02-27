from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            d[s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in d.values() if v > 1))
    return anagram_pairs <= 30