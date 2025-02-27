from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_counts[''.join(sorted(s))] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs >= 209