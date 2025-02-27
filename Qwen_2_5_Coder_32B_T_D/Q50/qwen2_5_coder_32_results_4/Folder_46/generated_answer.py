from collections import Counter

def if_contains_anagrams(words):
    word_counts = Counter((''.join(sorted(w.lower())) for w in words if len(w) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in word_counts.values() if v > 1))
    return anagram_pairs >= 38