from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagram_counts[s] += 1
    total_anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return total_anagram_pairs <= 94