from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            anagram_counts[''.join(sorted(s))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values() if v > 1))
    return anagram_pairs >= 19