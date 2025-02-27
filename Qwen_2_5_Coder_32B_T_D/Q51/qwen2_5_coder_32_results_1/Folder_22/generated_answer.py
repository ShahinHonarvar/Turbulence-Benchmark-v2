from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_counts[w] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pair_count <= 14