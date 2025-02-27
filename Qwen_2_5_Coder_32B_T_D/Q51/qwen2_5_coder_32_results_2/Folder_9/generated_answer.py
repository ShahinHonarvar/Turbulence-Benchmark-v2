from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    words = [w.lower() for w in words if len(w) >= 3]
    anagram_counts = Counter((''.join(sorted(w)) for w in words))
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return anagram_pairs <= 475