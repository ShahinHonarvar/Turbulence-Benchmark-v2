from collections import defaultdict

def if_contains_anagrams(words):
    counts = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            counts[w] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return anagram_pairs >= 42