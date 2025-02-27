from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagrams[w] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return pair_count <= 43