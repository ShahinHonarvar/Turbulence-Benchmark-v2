from collections import Counter, defaultdict

def if_contains_anagrams(lst):
    anagram_counts = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_counts[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 108