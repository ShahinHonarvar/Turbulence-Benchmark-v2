from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_counts[sorted_s] += 1
    pairs_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs_count >= 24