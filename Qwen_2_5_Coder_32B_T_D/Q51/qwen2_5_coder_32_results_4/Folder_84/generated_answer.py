from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            anagrams[tuple(sorted(word))] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pair_count <= 16