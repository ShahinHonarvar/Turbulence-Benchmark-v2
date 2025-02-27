from collections import Counter

def if_contains_anagrams(words):
    anagram_counts = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    return sum((v * (v - 1) // 2 for v in anagram_counts.values())) <= 147