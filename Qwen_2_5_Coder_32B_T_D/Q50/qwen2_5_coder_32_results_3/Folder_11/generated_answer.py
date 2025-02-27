from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s_lower = ''.join(sorted(s.lower()))
        if len(s_lower) >= 3:
            anagram_counts[s_lower] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 28