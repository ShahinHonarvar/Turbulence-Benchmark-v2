from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_counts[sorted_s] += 1
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) >= 16