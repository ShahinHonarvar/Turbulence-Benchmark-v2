from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_count[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return pairs >= 43