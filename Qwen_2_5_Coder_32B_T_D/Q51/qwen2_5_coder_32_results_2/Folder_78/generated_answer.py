from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_counts[''.join(sorted(s))] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count <= 70