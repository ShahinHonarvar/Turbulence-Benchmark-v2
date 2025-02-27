from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_counts[sorted_s] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count <= 67