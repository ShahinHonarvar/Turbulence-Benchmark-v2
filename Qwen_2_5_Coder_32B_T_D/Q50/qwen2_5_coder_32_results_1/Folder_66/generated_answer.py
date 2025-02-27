from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_counts[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 92